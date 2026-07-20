/**
 * build-cv-latex.test.mjs — regression tests for build-cv-latex.mjs's bullet
 * rendering, specifically the 'bullet' mode of escapeLatex(), which is what
 * lets tailored CVs highlight key metrics/skills the same way the
 * hand-written master resume does (**text** -> \textbf{text}).
 *
 * Run: node build-cv-latex.test.mjs
 */

import { escapeLatex } from './build-cv-latex.mjs';

let passed = 0;
let failed = 0;
const failures = [];

function eq(label, actual, expected) {
  if (actual === expected) {
    passed++;
  } else {
    failed++;
    failures.push(label);
    console.log(`  FAIL: ${label}`);
    console.log(`    expected: ${JSON.stringify(expected)}`);
    console.log(`    actual:   ${JSON.stringify(actual)}`);
  }
}

eq(
  'single bold span becomes \\textbf{}',
  escapeLatex('Reduced **latency** by 40%', 'bullet'),
  'Reduced \\textbf{latency} by 40\\%'
);

eq(
  'multiple bold spans in one bullet all convert',
  escapeLatex('Built **gRPC layer** achieving **99.9% uptime**', 'bullet'),
  'Built \\textbf{gRPC layer} achieving \\textbf{99.9\\% uptime}'
);

eq(
  'plain bullet text with no bold markers is unaffected (matches text mode)',
  escapeLatex('Diagnosed N+1 query bottleneck', 'bullet'),
  escapeLatex('Diagnosed N+1 query bottleneck', 'text')
);

eq(
  'special LaTeX characters inside a bold span are still escaped',
  escapeLatex('Cut cost by **44% ($40-60/mo)**', 'bullet'),
  'Cut cost by \\textbf{44\\% (\\$40-60/mo)}'
);

eq(
  'unmatched trailing ** does not crash and is left literal',
  escapeLatex('Shipped feature **', 'bullet'),
  'Shipped feature **'
);

eq(
  'bullet mode on non-string input returns empty string like text mode',
  escapeLatex(undefined, 'bullet'),
  ''
);

console.log(`\n${passed} passed, ${failed} failed`);
if (failed > 0) {
  console.log('Failures:', failures.join(', '));
  process.exit(1);
}
process.exit(0);
