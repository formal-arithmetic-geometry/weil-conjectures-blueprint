+++
kind = "proof"
of = "sk-p-dl-general-relative-line"
uses = ["sk-thm-wft-curve-middle-upper"]
+++
We bound the stalks of $R^ih_!F$ by the curve case, show that these
sheaves are mixed by twisting to weight zero and adding the dual, as
explained at the
start of this section, and combine the two facts using
Lemma [sk-lem-wgen-punctual-cutoff].

*The stalks.* Fix a closed point $y$ of $Y_0$. Base change for
direct images with compact support
(Proposition [sk-thm-sf-comp-composition]) identifies

$$
(R^ih_!F)_{\bar y}=H_c^i(U_{\bar y},F)
$$

together with its local Frobenius operator. The restriction of $F$ to
the fibre is again pure of weight $w$, because a residue extension
raises both an eigenvalue and the residue cardinality to the same
power. The fibre is a smooth affine curve over $\kappa(y)$, and
Theorem [sk-thm-wft-curve-middle-upper] shows that $H_c^i(U_{\bar y},F)$ has
weights at most $w+i$. After a finite extension of $\kappa(y)$ the
components of the fibre are geometrically connected, and
Lemma [sk-l-dl-a1-endpoints], applied to each of them with $j$ the
identity, shows that these groups vanish outside degrees $1$ and
$2$.

*Mixedness.* Next we prove that $R^ih_!F$ is mixed. Since the
assertion is trivial for $F=0$, we may
assume $F\ne0$. Let $G=F^0\oplus(F^0)^\vee$, with
$F^0=F\otimes\mathcal B_b$, be the sheaf of
Proposition [sk-prop-wrp-real-envelope]; it is lisse, real and pure of
weight zero. At a closed point $y$
write

$$
P_{i,y}(T)=\det(1-T\operatorname{Frob}_y\mid H_c^i(U_{\bar y},G)).
$$

Applying Lemma [sk-l-dl-a1-endpoints] to the components of the
fibre after a finite extension of $\kappa(y)$, as above, we see that
$P_{0,y}=1$ and that every reciprocal root of $P_{2,y}$ has modulus
$q_y$. By the bound just proved, every reciprocal root of $P_{1,y}$
has modulus at most $q_y^{1/2}$.

We claim that $\iota P_{1,y}$ and $\iota P_{2,y}$ have real
coefficients. By the Euler product and the determinant identity of
Theorem [sk-thm-trace-transport], after applying $\iota$ we have

$$
L_\iota(U_y,G,T)=\frac{\iota P_{1,y}(T)}{\iota P_{2,y}(T)}.
$$

Since the Euler factors are real, this rational function has real
Taylor coefficients. Hence it equals its complex conjugate as a
rational function, both being regular at zero. The numerator and the
denominator are coprime, because a common root would give an
eigenvalue having both permitted moduli, whereas $q_y^{1/2}<q_y$.
A reduced fraction whose numerator and denominator have constant
coefficient one is unique, and comparing it with its conjugate we
find $\iota P_{1,y},\iota P_{2,y}\in\mathbf R[T]$. This proves the
claim. Therefore the sheaves $R^ih_!G$, which are constructible by the
finiteness theorems, are real at every closed point, and
Theorem [sk-i-dl-general-real] gives a finite mixed filtration of
each of them.

By additivity, $R^ih_!F^0$ is a direct summand of $R^ih_!G$, and hence
it is mixed. The projection formula for the constant twist identifies
it with $R^ih_!F\otimes\mathcal B_b$. Removing the twist shifts the weight of
every pure quotient by $w$ and preserves the finite Weil filtration,
and so $R^ih_!F$ is mixed.

*Conclusion.* The bound on the stalks proved above and
Lemma [sk-lem-wgen-punctual-cutoff] show that every nonzero quotient in
this filtration has weight at most $w+i$.
