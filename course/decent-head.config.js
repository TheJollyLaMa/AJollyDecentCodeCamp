window.DECENT_CONFIG = {
  appName: 'Decent Code Camp',
  subtitle: 'Ideas, practice and a first dapp',
  chain: null,
  ens: { enabled: false },
  theme: { 'bg-1': '#12303a', 'bg-2': '#1c4b50', accent: '#a6e8d4', 'accent-2': '#efbd75' },
  ipfsAdapter: { version: 1, label: 'Course materials', capabilities: {}, getStatus: async () => ({}) },
  about: {
    title: 'About Decent Code Camp',
    summary: 'A prepared 12-week path from an idea to a tested Web3 prototype.',
    sections: [
      { title: 'Pilot, not enrollment', body: 'The course and facilitator-led pilot are prepared material. No cohort, enrollment or checkout is active.' },
      { title: 'Your data and wallet', body: 'A wallet is optional. This header does not upload learner data. Provider selection does not verify a backup. UCAN authorization is not implemented.' }
    ]
  },
  links: [{ label: 'Course source', url: 'https://github.com/TheJollyLaMa/AJollyDecentCodeCamp' }]
};
