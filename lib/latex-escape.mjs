/**
 * Shared LaTeX escaping for career-ops CV scripts.
 */

/**
 * Escape user text for insertion into LaTeX macro arguments.
 *
 * @param {string} text
 * @param {'text'|'url'|'bullet'} [mode='text']
 * @returns {string}
 */
export function escapeLatex(text, mode = 'text') {
  if (typeof text !== 'string') return '';
  if (mode === 'url') return text;
  if (mode === 'bullet') return escapeBulletText(text);
  return escapePlain(text);
}

function escapePlain(text) {
  const out = [];
  for (const ch of text) {
    switch (ch) {
      case '\\': out.push('\\textbackslash{}'); break;
      case '{': case '}': out.push('\\' + ch); break;
      case '^': out.push('\\textasciicircum{}'); break;
      case '~': out.push('\\textasciitilde{}'); break;
      case '_': out.push('\\_'); break;
      case '&': out.push('\\&'); break;
      case '%': out.push('\\%'); break;
      case '$': out.push('\\$'); break;
      case '#': out.push('\\#'); break;
      case '\u00B1': out.push('$\\pm$'); break;
      case '\u2192': out.push('$\\rightarrow$'); break;
      default: out.push(ch);
    }
  }
  return out.join('');
}

/**
 * Escape achievement/bullet text, converting `**bold**` markdown to a real
 * `\textbf{}` command. Segments outside `**...**` are escaped normally;
 * text inside `**...**` is escaped the same way and wrapped in a literal
 * (unescaped) `\textbf{}` so the LaTeX command itself survives.
 */
function escapeBulletText(text) {
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  return parts
    .map((part) => {
      const boldMatch = part.match(/^\*\*([^*]+)\*\*$/);
      if (boldMatch) return `\\textbf{${escapePlain(boldMatch[1])}}`;
      return escapePlain(part);
    })
    .join('');
}

/**
 * Validate and normalize URLs for \\href{} (not LaTeX-escaped).
 *
 * @param {string} url
 * @returns {string}
 */
export function sanitizeUrl(url) {
  if (typeof url !== 'string') return '';
  url = url.trim();
  if (!url) return '';
  const allowedSchemes = ['mailto:', 'http:', 'https:'];
  const hasScheme = allowedSchemes.some(s => url.toLowerCase().startsWith(s));
  if (!hasScheme) {
    if (url.includes('@') && !url.includes('/')) {
      url = 'mailto:' + url;
    } else {
      url = 'https://' + url;
    }
  }
  return url.replace(/[{}%$#\\~^]/g, '');
}
