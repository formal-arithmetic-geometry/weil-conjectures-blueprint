+++
id = "thm-pqf-immersion-descent"
kind = "theorem"
title = "Descent of the immersion to a finite stage"
order = 206
uses = ["def-weil-pbc-scheme-conventions", "pqf-def-locnoeth", "pqf-def-quasifinite", "pqf-lem-finite-fp-locnoeth", "pqf-lem-limit-immersion-descends", "pqf-lem-limit-qc-open-descends", "pqf-lem-qs-intersection-qc"]
+++
Let $f:X\to S$ be a separated morphism of finite type which is
everywhere quasi-finite, with $S$
quasi-compact and quasi-separated. Let $\nu_f:N_f\to S$ be the
relative normalization of $S$ in $X$, with $X\xrightarrow{\iota_f} N_f$ a quasi-compact open immersion, and let
$N_f=\varprojlim_\lambda T_\lambda$ be the presentation of $N_f$ as a
filtered limit of finite $S$-schemes, with affine transition maps,
supplied by the finite-approximation tail of the preceding proof. Then
there are an index $\lambda_0$ and a factorization

$$
X\xrightarrow{\ j\ }T\xrightarrow{\ i\ }T_{\lambda_0}
$$

with $j$ a quasi-compact open immersion and $i$ a closed immersion.
If moreover $S$ is
locally Noetherian — in particular if
$f$ is locally of finite presentation over a locally Noetherian
$S$ — the index $\lambda_0$ may be chosen so that
$T_{\lambda_0}$ is finite and of finite presentation over $S$.

Descending only the open subscheme $\iota_f(X)$ to an open
$U\subseteq T_{\lambda_0}$ does not suffice: it exhibits $X$ as the fibre
product $N_f\times_{T_{\lambda_0}}U$, whose projection onto $U$ is the base
change of the integral morphism $\nu_f$, hence finite and surjective of the
same degree as $\nu_f$, and therefore not an immersion as soon as one fibre
of $\nu_f$ over $U$ has more than one point. What is needed in addition is
the spreading out of the *closed* immersion $X\to U$. For $f$ locally of
finite presentation over a general quasi-compact quasi-separated $S$, the
finite-presentation clause is not claimed for a stage of this
presentation, whose transition maps are dual to injective algebra maps
$\mathcal A_\lambda\hookrightarrow\mathcal A_\mu$ rather than closed
immersions. It holds in a corrected form: the finite scheme $T$ of the
factorization can be replaced by a finite and finitely presented
$S$-scheme containing $X$ as a quasi-compact open subscheme. Over a
locally Noetherian $S$ the clause holds for the presentation itself,
because every finite $S$-scheme is then of finite presentation.
