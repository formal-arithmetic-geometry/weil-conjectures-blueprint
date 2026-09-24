+++
id = "pqf-rem-fp-stage-status"
kind = "remark"
title = "Status of the finite-presentation clause of the interface"
order = 2015
uses = ["pqf-def-locnoeth", "pqf-lem-finite-fp-locnoeth", "pqf-thm-zmt-fp", "thm-pqf-immersion-descent"]
+++
[pqf-thm-zmt-fp] settles the finiteness-and-finite-presentation
clause of [thm-pqf-immersion-descent] for a morphism $f$ which is
locally of finite presentation over a general quasi-compact
quasi-separated $S$, in the following sense: the finite scheme
$T_{\lambda_0}$ of clause (i) is replaced by a finite and finitely
presented $S$-scheme $T$ containing $X$ as a quasi-compact open
subscheme, so that $X\xrightarrow{j}T\xrightarrow{\mathrm{id}}T$ is a
factorization with $j$ a quasi-compact open immersion and the identity
a closed immersion. That stage is an index of the presentation of the
finite scheme $T_0$ supplied by Tag 09YY; it is *not* a stage of
the presentation $N_f=\varprojlim_\lambda T_\lambda$ of the
finite-approximation tail, and for that presentation the clause is not
asserted here: the tail's transition morphisms are affine and dual to the
injective algebra maps $\mathcal A_\lambda\hookrightarrow\mathcal A_\mu$, so that they are closed immersions only when the two stages
coincide, whereas Tag 09YY concludes precisely that its stages are
finitely presented and its transition maps are closed immersions. Over a
locally Noetherian $S$ the clause does hold
for the tail itself, by [pqf-lem-finite-fp-locnoeth]: a finite
$S$-scheme is then automatically of finite presentation over $S$.
