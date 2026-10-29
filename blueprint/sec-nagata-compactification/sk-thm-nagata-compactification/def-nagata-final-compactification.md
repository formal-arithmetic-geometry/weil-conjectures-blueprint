+++
id = "def-nagata-final-compactification"
kind = "definition"
title = "Final Nagata compactification candidate"
order = 405
lean = ["AlgebraicGeometry.fpEnvelopeCompactification", "AlgebraicGeometry.constructedCompactification", "AlgebraicGeometry.NagataCompactification"]
uses = ["def-nagata-closed-subscheme-compactification", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-final-basechanged-compactification", "def-nagata-final-fp-envelope", "lemma-nagata-final-basechanged-compactification", "lemma-nagata-final-fp-envelope", "prop-nagata-closed-subscheme-compactifiable", "prop-nagata-finite-type-closed-in-fp"]
+++
Let $S$ be quasi-compact and quasi-separated and let $f\colon X\to S$ be
separated, quasi-compact and locally of finite type. By
[lemma-nagata-final-fp-envelope], [def-nagata-final-basechanged-compactification]
applies to $Y=X_f^{\mathrm{fp}}$; write
$C_f^{\mathrm{fp}}=\mathsf C^{\mathrm{fp}}(X_f^{\mathrm{fp}}/S)
=\bigl(X_f^{\mathrm{fp}}\hookrightarrow
\overline X_f^{\mathrm{fp}}\longrightarrow S\bigr)$ and

$$
\mathsf{Closed}(i_f^{\mathrm{fp}},C_f^{\mathrm{fp}})
=\bigl(X\xrightarrow{j^{\mathrm{cl}}_f}\overline X^{\mathrm{cl}}_f
\xrightarrow{p^{\mathrm{cl}}_f}S\bigr).
$$

This constructed factorization is a compactification
of $f$ in the sense of [def-nagata-compactification], so $f$ is
compactifiable. Define

$$
\mathsf C_{\mathrm{Nag}}(f)
=\bigl(X\xrightarrow{j_f}\overline X_f
\xrightarrow{p_f}S\bigr)
$$

to be a chosen compactification of $f$: a scheme $\overline X_f$, an open
immersion $j_f$ and a proper morphism $p_f$ with $f=p_f\circ j_f$.
