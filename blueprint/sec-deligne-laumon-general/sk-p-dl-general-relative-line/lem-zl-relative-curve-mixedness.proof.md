+++
kind  = "proof"
of    = "lem-zl-relative-curve-mixedness"
uses = ["sk-thm-sf-ctf-stability", "sk-prop-wrp-real-envelope", "def-wf-normalized-real-envelope", "lem-wf-envelope-real", "lem-zl-relative-envelope-factor-reality", "thm-zl-real-mixed-by-curves"]
+++
If $\mathcal F=0$ there is nothing to prove; otherwise choose a closed
point $x$, of degree $d$, at which the stalk is nonzero, and a Frobenius
eigenvalue $\alpha$ there. As in [sk-prop-wrp-real-envelope], let
$b\in\Qlb^\times$ be a $d$th root of $\alpha^{-1}$; by purity
$|\iota(b)|=|\iota(\alpha)|^{-1/d}=q^{-w/2}$. This uses only that
$\iota$ is a field embedding, not that it is surjective. Normalize
$\mathcal F$ as in [def-wf-normalized-real-envelope]: put
$\mathcal F^0=\mathcal F\otimes\mathcal B_b$, and
$\mathcal E=\mathcal F^0\oplus(\mathcal F^0)^\vee$.
It is lisse, pure of weight zero and real by
[lem-wf-envelope-real]. The relative factor calculation
[lem-zl-relative-envelope-factor-reality], which uses only the
proved curve estimate, shows that $R^ih_!\mathcal E$ is real for
every $i$. These are constructible sheaves: $Rh_!$ preserves
$\Dbc(-,\Qlb)$ by [sk-thm-sf-ctf-stability], so each
$R^ih_!\mathcal E$ lies in $\Cons(Y,\Qlb)$, and it inherits a Weil
structure from that of $\mathcal E$.

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
