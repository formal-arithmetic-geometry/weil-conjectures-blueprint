+++
kind  = "proof"
of    = "thm-nagata-compactification"
+++
By [prop-nagata-finite-type-closed-in-fp], $f$ factors as the closed
immersion $i_f^{\mathrm{fp}}\colon X\hookrightarrow X_f^{\mathrm{fp}}$
followed by a separated morphism $X_f^{\mathrm{fp}}\to S$ of finite
presentation; in particular $X_f^{\mathrm{fp}}\to S$ is quasi-compact. By
[lemma-nagata-final-basechanged-compactification], $X_f^{\mathrm{fp}}\to S$
has the compactification $C_f^{\mathrm{fp}}$. Consider the constructed
factorization
$\mathsf{Closed}(i_f^{\mathrm{fp}},C_f^{\mathrm{fp}})
=(X\xrightarrow{j^{\mathrm{cl}}_f}\overline X^{\mathrm{cl}}_f
\xrightarrow{p^{\mathrm{cl}}_f}S)$ of [def-nagata-final-compactification].
Its first map is a (quasi-compact) open immersion by
[lemma-nagata-final-open-immersion]; its second map is proper by
[lemma-nagata-final-ambient-proper]; and their composite is $f$ by
[lemma-nagata-final-factorization]. These are exactly the fields of
[def-nagata-compactification] (this is also the content of
[prop-nagata-closed-subscheme-compactifiable] applied to
$i_f^{\mathrm{fp}}$ and $C_f^{\mathrm{fp}}$). Hence $f$ admits a
compactification, i.e. $f$ is compactifiable in the sense of
[def-nagata-compactifiable]. Consequently the chosen compactification
$\mathsf C_{\mathrm{Nag}}(f)$ of [def-nagata-final-compactification] is
defined, and by definition it consists of an open immersion
$j_f\colon X\to\overline X_f$ and a proper morphism
$p_f\colon\overline X_f\to S$ with $f=p_f\circ j_f$.
