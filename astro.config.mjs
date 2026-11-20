import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({
  site: 'https://masjidee.github.io',
  base: '/',
  trailingSlash: 'always',
  integrations: [starlight({
    title: 'Masjidee guides',
    description: 'Help with prayer times, mosque activities, learning and privacy in the Masjidee pilot.',
    logo: { src: './public/masjidee-mark.svg', replacesTitle: false },
    favicon: '/masjidee-mark.svg',
    customCss: ['./src/styles/docs.css'],
    social: [{ icon: 'github', label: 'Website source', href: 'https://github.com/masjidee/masjidee.github.io' }],
    sidebar: [
      { label: 'Welcome', link: '/docs/' },
      { label: 'Start here', items: [
        { label: 'Getting started', link: '/docs/guides/getting-started/' },
        { label: 'Install the Android pilot', link: '/docs/guides/install-android/' },
        { label: 'Choose your mosque', link: '/docs/guides/choose-mosque/' },
      ]},
      { label: 'Everyday use', items: [
        { label: 'Prayer times & reminders', link: '/docs/guides/prayers/' },
        { label: 'Activities & calendars', link: '/docs/guides/calendars/' },
        { label: 'Check-ins & automatic detection', link: '/docs/guides/check-ins/' },
        { label: 'Attendance reports', link: '/docs/guides/attendance/' },
        { label: 'Learning & Friday sermons', link: '/docs/guides/learning/' },
        { label: 'Find the Qibla', link: '/docs/guides/qibla/' },
      ]},
      { label: 'Help & privacy', items: [
        { label: 'Troubleshooting', link: '/docs/guides/troubleshooting/' },
        { label: 'Privacy & permissions', link: '/docs/guides/privacy/' },
        { label: 'What is available?', link: '/docs/guides/availability/' },
      ]},
      { label: 'For administrators', items: [
        { label: 'Mosque settings & calendars', link: '/docs/admin/mosque-settings/' },
        { label: 'Web attendance reports', link: '/docs/admin/attendance/' },
      ]},
    ],
  })],
});
