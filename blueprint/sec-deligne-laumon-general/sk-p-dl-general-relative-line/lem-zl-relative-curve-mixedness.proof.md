+++
kind  = "proof"
of    = "lem-zl-relative-curve-mixedness"
uses = ["def-wf-normalized-real-envelope", "lem-wf-envelope-real", "lem-zl-relative-envelope-factor-reality", "thm-zl-real-mixed-by-curves"]
+++
Normalize $\mathcal F$ as in
[def-wf-normalized-real-envelope]: put
$b=\iota^{-1}(q^{-w/2})$,
$\mathcal F^0=\mathcal F\otimes\mathcal B_b$, and
$\mathcal E=\mathcal F^0\oplus(\mathcal F^0)^\vee$.
It is lisse, pure of weight zero and real by
[lem-wf-envelope-real]. The relative factor calculation
[lem-zl-relative-envelope-factor-reality], which uses only the
proved curve estimate, shows that $R^ih_!\mathcal E$ is real for
every $i$. These are constructible sheaves: the finite-level
finiteness theorem [sbc-thm-finiteness-finite-type] supplies the
constructible landing hypotheses in the coefficient passage of
[thm-cbc-qbar].

Apply [thm-zl-real-mixed-by-curves] on $Y_0$, obtaining a
finite mixed filtration of $R^ih_!\mathcal E$.
Additivity makes $R^ih_!\mathcal F^0$ a direct summand, so it is
mixed by [lem-a1-mixed-direct-summand]. The constant-twist
projection formula [lem-wf-constant-twist-cohomology] identifies

$$
R^ih_!\mathcal F
\cong R^ih_!\mathcal F^0\otimes\mathcal B_{b^{-1}}.
$$

Tensoring the finite filtration with this rank-one sheaf is exact.
At a closed point of degree $m$, the twist multiplies each
eigenvalue by $b^{-m}$, of $\iota$-modulus $q^{mw/2}$, by
[def-wf-constant-weil-twist]. Thus every pure quotient of weight
$v$ becomes pure of weight $v+w$, including where its stalk is
zero. This gives the required finite mixed filtration without a
lissity assumption on the direct image. Its finitely many
weights have a maximum $u_i$; for the zero sheaf take any $u_i$.
