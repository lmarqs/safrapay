import { defineConfig } from 'orval';

export default defineConfig({
  safrapay: {
    input: { target: 'generated/openapi.bundled.yaml' },
    output: {
      target: 'generated/node/main.ts',
      mode: 'split',
      client: 'fetch',
      httpClient: 'fetch',
    },
  },
});
