+++
kind  = "proof"
of    = "sk-p-dl-a1-some-weight"
+++
We follow the construction of the real envelope
([sk-prop-wrp-real-envelope]), with the Fourier kernel
$\mathcal K_\psi$ of [sk-thm-inversion] included.
Choose a closed point $x$ of $U_0$, of degree $d$, and a
Frobenius eigenvalue $\alpha$ on $M_{\bar x}$. Choose
$b\in\Qlb^\times$ with $b^d=\alpha^{-1}$, and let
$\mathcal B_b$ be the constant Weil line whose Frobenius is $b$.
Then $|\iota b|=q^{-w/2}$, so $M^0=M\otimes\mathcal B_b$
is pure of weight zero.

On the product of the line and the dual line, consider the sheaf

$$
 \mathcal E=
 (p_1^*j_!M^0\otimes\mathcal K_\psi)
 \ \oplus\
 (p_1^*j_!(M^0)^\vee\otimes\mathcal K_{\psi^{-1}}).
$$

The local spectra of the two summands are complex conjugate, because
the eigenvalues of $M^0$ have absolute value one and the eigenvalues of
the character sheaves are roots of unity ([sk-lem-as-properties]). At
the boundary both zero extensions have zero stalks. Thus $\mathcal E$
is real in the sense of [sk-def-wrp-real-definition]. The dual
$(M^0)^\vee$ is also Fourier-generic, since duality replaces a
geometric constituent $\mathcal L_{\psi(ax)}$ by
$\mathcal L_{\psi(-ax)}$, that is, $a$ by $-a$; and so the argument of
[sk-p-dl-a1-correction] applies to both summands and shows that the
compact-support direct image of $\mathcal E$ along $p_2$ is
concentrated in degree one. Set $H=R^1p_{2!}\mathcal E$.

At every finite-field point $y$, the trace formula
([sk-thm-tf-uniform-formula]) writes $-t_H(y)$ as a sum of conjugate
pairs, and the same holds for every power of the local Frobenius. By
the Newton identities, the local characteristic polynomials of $H$
have real coefficients.

Choose a dense open on which both $H$ and $M'$ are lisse.
By the projection formula and [sk-p-dl-a1-correction],
$M'\otimes\mathcal B_b$ is a quotient of a direct summand of $H$
there, and it is irreducible by [sk-lem-wft-curve-simples].
[sk-p-real-purity] shows that this quotient is pure of some
real weight, and untwisting we find that $M'$ is pure of some weight
$v$ on that open.

Consider a remaining point of the open where $M'$ is lisse. There,
boundary semicontinuity ([sk-p-real-semi]) bounds the stalk weights of
$M'$ by $v$ and those of its dual by $-v$, since the middle extensions
of these sheaves from the smaller open recover their lisse stalks. The
two bounds together show, as in [sk-cor-wrp-unramified-purity], that
$M'$ is pure of weight $v$ on the whole open.
