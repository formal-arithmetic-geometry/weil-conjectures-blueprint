+++
id = "the-picard-scheme-of-a-curve"
kind = "section"
title = "The Picard scheme of a curve"
order = 4200
+++
Outline module 3: cohomology and base change, descent, and
representability. Together with the algebraic-group results this supplies
the Jacobian used in the Jacobian chapter.

The chapter is a converted standalone file: its preamble, private macro
block, and the "Basic blocks" section (the blocks of the earlier chapters
reproduced with their original labels) were removed, so that the labels
`def:weil-pbc-*`, `def:sc-*`, `lem:sc-*`, `thm:sc-*` refer to those
chapters; the duplicate smoothness definition is replaced by the framework
chapter's `def:weil-scheme-morphism-properties`, and all private macros
were inlined. The source's Mathlib marks are kept and appear as `lean`
names on the five objects that carry them.

Section order follows the source: each section stands after the material it
uses. The source records 46 forward references inside the chapter both
before and after the ordering, and that its sections 2--10 were permuted.
