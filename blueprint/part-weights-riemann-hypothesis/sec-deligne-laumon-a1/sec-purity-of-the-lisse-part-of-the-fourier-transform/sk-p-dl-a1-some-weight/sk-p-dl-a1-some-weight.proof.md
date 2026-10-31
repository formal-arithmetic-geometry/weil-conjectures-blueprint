+++
kind = "proof"
of = "sk-p-dl-a1-some-weight"
uses = ["sk-r-real-linear", "sk-lem-wrp-twisted-envelope", "sk-cor-tf-trace-function-pushforward"]
+++
We twist to weight zero and add the dual, as in
Proposition [sk-prop-wrp-real-envelope], before taking the transform, so
that a twist of $M'$ becomes a quotient of a real sheaf, to which
Theorem [sk-p-real-purity] applies. Choose a closed point $x$ of $U_0$, of degree $d$, and a
Frobenius eigenvalue $\alpha$ on $M_{\bar x}$. Choose
$b\in \overline{\mathbf Q}_\ell^\times$ with $b^d=\alpha^{-1}$, and let
$\mathcal B_b$ be the geometrically constant rank-one Weil sheaf of
Proposition [sk-r-real-linear], on which Frobenius acts by $b$.
Then $|\iota b|=q^{-w/2}$, so $M^0=M\otimes\mathcal B_b$
is pure of weight zero.

On the product of the line and the dual line, consider the sheaf

$$
F=
(p_1^*j_!M^0\otimes\mathcal K_\psi)
\ \oplus\
(p_1^*j_!(M^0)^\vee\otimes\mathcal K_{\psi^{-1}}).
$$

At each closed point, the Frobenius eigenvalues of the second summand
are the complex conjugates of those of the first, because the
eigenvalues of $M^0$ have absolute value one and those of the
character sheaves are roots of unity. At the boundary both zero
extensions have zero stalks. Hence $F$ is real, as in
Lemma [sk-lem-wrp-twisted-envelope]. The dual
$(M^0)^\vee$ also has no geometric constituent of the form
$\mathcal L_{\psi(ax)}$, since duality replaces $a$ by $-a$. Therefore the argument of Lemma [sk-p-dl-a1-correction] shows
that the direct image with compact support of $F$ along $p_2$
is concentrated in degree one. Set $H=R^1p_{2!}F$.

Let $y$ be a point with values in a finite field. Since
$Rp_{2!}F=H[-1]$, the trace formula for $Rp_{2!}$
(Corollary [sk-cor-tf-trace-function-pushforward]) gives
$-t_H(y)=\sum_x t_F(x,y)$, and for each $x$ the traces of
the two summands of $F$ at $(x,y)$ are complex conjugate.
Hence $t_H(y)$ is real, and the same holds for every power of the
local Frobenius. It follows from the Newton
identities that the local characteristic polynomials of $H$ have real
coefficients.

The first summand of $H$ is
$R^1p_{2!}(p_1^*j_!M\otimes\mathcal K_\psi)\otimes\mathcal B_b$ by the
projection formula for the constant twist, that is, $G\otimes\mathcal B_b$
with $G=\operatorname{FT}_\psi(j_!M)$ as in
Lemma [sk-p-dl-a1-correction]. The surjection $G\to j'_*M'$ of that
lemma therefore makes $M'\otimes\mathcal B_b$ a quotient of a direct
summand of $H$ on a dense open on which both $H$ and $M'$ are lisse,
and it is irreducible there by Lemma [sk-lem-wft-curve-simples]. Since
$H$ is real, Theorem [sk-p-real-purity] shows that this quotient is
pure of some real weight. Removing the twist by $\mathcal B_b$, we
find that $M'$ is pure of some weight $v$ on that open. The open
where $M'$ is lisse is a smooth geometrically connected curve, and so
the last assertion of Corollary [sk-cor-wrp-unramified-purity] extends
the purity to all of it.
