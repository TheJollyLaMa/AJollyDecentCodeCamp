"use strict";

const assert = require("node:assert/strict");
const { readFileSync, existsSync } = require("node:fs");
const path = require("node:path");
const test = require("node:test");

const root = path.join(__dirname, "..");
const entryPath = path.join(root, "course/index.html");
const guidePath = path.join(root, "course/12-week-dapp-course.md");
const entry = readFileSync(entryPath, "utf8");
const guide = readFileSync(guidePath, "utf8");

function stripTags(markup) {
  return markup.replace(/<[^>]*>/g, " ").replace(/&amp;/g, "&").replace(/\s+/g, " ").trim();
}

function extractWeekCards(markup) {
  return [...markup.matchAll(/<li class="week">([\s\S]*?)<\/li>/g)].map((match) => {
    const body = match[1];
    const title = stripTags(body.match(/<h3>([\s\S]*?)<\/h3>/)?.[1] || "");
    const field = (name) => {
      const fieldMatch = body.match(new RegExp(`<strong>${name}:<\\/strong>([\\s\\S]*?)(?=<\\/p>)`));
      return stripTags(fieldMatch?.[1] || "");
    };
    return {
      title,
      outcome: field("Outcome"),
      exercise: field("Exercise"),
      evidence: field("Evidence"),
    };
  });
}

test("course has exactly 12 numbered weeks with nonempty outcomes, exercises, and evidence checks", () => {
  const weeks = extractWeekCards(entry);
  assert.equal(weeks.length, 12);
  weeks.forEach((week, index) => {
    assert.match(week.title, new RegExp(`^${index + 1} · .+`));
    assert.ok(week.outcome.length > 10, `week ${index + 1} needs an outcome`);
    assert.ok(week.exercise.length > 10, `week ${index + 1} needs a concrete exercise`);
    assert.ok(week.evidence.length > 10, `week ${index + 1} needs an evidence check`);
  });
});

test("course entry and guide link to the current-main teaching example", () => {
  assert.match(entry, /href="12-week-dapp-course\.md"/);
  assert.ok(existsSync(guidePath));
  const markdownLinks = [...guide.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)].map((match) => match[1]);
  const localLinks = markdownLinks.filter((url) => !/^(?:https?:|mailto:|#)/i.test(url));
  assert.ok(localLinks.length >= 2, "guide should link to local course material and the current teaching example");
  for (const url of localLinks) {
    assert.ok(existsSync(path.resolve(path.dirname(guidePath), url)), `guide link does not exist on this branch: ${url}`);
  }
  assert.ok(localLinks.includes("../Class1/Fibonacci/Fibonacci.py"));
  const lessonLinks = [...entry.matchAll(/href="https:\/\/github\.com\/TheJollyLaMa\/AJollyDecentCodeCamp\/blob\/main\/([^"]+)"/g)]
    .map((match) => match[1]);
  assert.ok(lessonLinks.includes("Class1/Fibonacci/Fibonacci.py"));
  for (const lessonPath of lessonLinks) {
    assert.ok(existsSync(path.join(root, lessonPath)), `course entry lesson does not exist on this branch: ${lessonPath}`);
  }
  assert.match(guide, /does not restore the older `jolly-brancher`/);
  assert.doesNotMatch(guide, /\.\.\/Class[234]\//);
});

test("pilot offer states its fee, format, payment/refund terms, and public inquiry without success claims", () => {
  const offer = stripTags(entry.match(/<div class="offer">([\s\S]*?)<\/div>/)?.[1] || "");
  const inquiry = entry.match(/<a class="button" href="([^"]+)">Ask about a future pilot<\/a>/);

  assert.match(offer, /USD \$240 per learner/);
  assert.match(offer, /90-minute/);
  assert.match(offer, /12 weeks/);
  assert.match(offer, /maximum 6 learners/);
  assert.match(offer, /manually issued invoice/);
  assert.match(offer, /due before the first session/);
  assert.match(offer, /full refund at least 7 calendar days/);
  assert.match(offer, /no refund is offered for sessions already held/);
  assert.match(offer, /No financial, employment, token, or income outcome is promised/);
  assert.ok(inquiry, "public pilot inquiry action is required");
  const inquiryUrl = new URL(inquiry[1].replace(/&amp;/g, "&"));
  assert.equal(inquiryUrl.origin, "https://github.com");
  assert.equal(inquiryUrl.pathname, "/TheJollyLaMa/AJollyDecentCodeCamp/issues/new");
  assert.match(decodeURIComponent(inquiryUrl.searchParams.get("body")), /issue is public/);
  assert.doesNotMatch(entry, /payment successful|enrollment confirmed|you are enrolled/i);
  assert.match(offer, /does not take payment or enroll anyone/);
  assert.match(entry, /No cohort dates, hosted course, payment checkout/);
});
