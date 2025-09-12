import type {ReactNode} from 'react';
import Layout from '@theme/Layout';

import Home from '../components/Home';

export default function HomePage(): ReactNode {
  return (
    <Layout
      title="도란보리"
      description="서울시립대 TTS 학술 소모임">
      <Home />
    </Layout>
  );
}
