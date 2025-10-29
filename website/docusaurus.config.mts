import { themes } from 'prism-react-renderer';

import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import tailwindPlugin from './plugins/tailwindPlugin';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const config: Config = {
  title: '도란보리',
  tagline: '서울시립대 TTS 학술 소모임',
  favicon: 'img/favicon.ico',
  url: 'https://doranbori.github.io/',
  baseUrl: '/doranbori-hub/',
  organizationName: 'doranbori',
  deploymentBranch: 'gh-pages',
  projectName: 'doranbori-hub',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'throw',
  future: {
    v4: {
      removeLegacyPostBuildHeadAttribute: true,
      useCssCascadeLayers: false,
    },
  },
  i18n: {
    defaultLocale: 'ko',
    locales: ['ko'],
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/doranbori/doranbori-hub/tree/main/website/',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex]
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl: 'https://github.com/doranbori/doranbori-hub/tree/main/website/',
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  plugins: [
    tailwindPlugin
  ],

  themeConfig: {
    navbar: {
      hideOnScroll: true,
      title: '도란보리',
      logo: {
        alt: 'DORANBORI LOGO',
        src: 'img/logo.svg',
        className: 'doranbori-nav-logo'
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Tutorial',
        },
        {
          to: '/blog', 
          label: 'Blog', 
          position: 'left'
        },
        {
          href: 'https://github.com/doranbori/doranbori-hub',
          position: 'right',
          className: 'header-github-link',
        },
      ],
    },
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    footer: {
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Tutorial',
              to: '/docs/startover',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Discord',
              href: 'https://discord.gg/2J3A2VuQU7',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'Github',
              href: 'https://github.com/doranbori/doranbori-hub'
            },
          ],
        },
      ],
      logo: {
        alt: 'DORANBORI LOGO',
        src: 'img/logo.svg',
        width: 40,
      },
      copyright: `Copyright © ${new Date().getFullYear()} - 도란보리`,
    },
    prism: {
      theme: themes.vsLight,
      darkTheme: themes.gruvboxMaterialDark,
    },
  } satisfies Preset.ThemeConfig,
  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
      type: 'text/css',
      integrity:
        'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM',
      crossorigin: 'anonymous',
    },
  ]
};

export default config;
