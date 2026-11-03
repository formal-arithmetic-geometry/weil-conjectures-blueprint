+++
kind  = "proof"
of    = "lem-fd-realified-kernel-real"
+++
Only the punctual purity of $\mathcal M$ is used below, which gives the
more general form of the statement.

Step 1 (the two summands are mutual conjugates). By
[lem-wf-pure-realizable] the local factor of
$\mathcal M^\dagger=\mathcal M^\vee\otimes\mathcal B_b$ at a closed point
$x$ of $U_0$ of degree $m$ has eigenvalues
$\iota(b^m\alpha^{-1})=q^{mw}\iota(\alpha)^{-1}=\overline{\iota(\alpha)}$,
where $\alpha$ runs through the eigenvalues of $F_x$ on
$\mathcal M_{\bar x}$: the eigenvalues of the twisted dual are exactly
the $\iota$-conjugates of those of $\mathcal M$, at every closed point.
The same computation applies to the extension by zero, since the stalk of
$j_!\mathcal M$ at a closed point of $\mathbf A^1_{k_0}$ is either the
stalk of $\mathcal M$ (over $U_0$) or zero. For the kernel factors, the
Artin–Schreier sheaf $\mathcal K_\psi$ of [def-fd-kernel] is lisse
of rank one ([lem-fd-as-lisse]) and punctually $\iota$-pure of
weight $0$ ([lem-fd-as-purity]), so its unique local eigenvalue
$\lambda$ at a closed point of the square satisfies
$|\iota(\lambda)|=1$ and therefore
$\overline{\iota(\lambda)}=|\iota(\lambda)|^2\iota(\lambda)^{-1} =\iota(\lambda)^{-1}$; by
$(\mathcal L_{\psi,f})^{-1}\cong\mathcal L_{\psi,-f}\cong\mathcal L_{\psi^{-1},f}$ of
[lem-fd-as-characters] the sheaf $\mathcal K_{\psi^{-1}}$ is the
inverse of $\mathcal K_\psi$ [prop-kernel-lisse], so its local eigenvalue at the same point
is $\lambda^{-1}$.

Step 2 (the realified kernel is real). Let $z$ be a closed point of the
Fourier square with first coordinate $x=p_1(z)$. If $x\in S_0$ then both
summands of $\mathcal K$ have zero stalk at $z$, because $j_!\mathcal M$
and $j_!(\mathcal M^\dagger)$ are extensions by zero from $U_0$; the
local factor of $\mathcal K$ at $z$ is then $1$, which is real. If
$x\in U_0$, let $e$ be the degree of $\kappa(z)$ over $\kappa(x)$ and let
$E$ be the multiset of eigenvalues of $F_x$ on $\mathcal M_{\bar x}$.
The local eigenvalues of the first summand at $z$ are
$\{\alpha^e\lambda:\alpha\in E\}$ — pullback along $p_1$ raises the local
Frobenius to the $e$-th power, which is the degree formula for the local
Frobenius [lem-trf-frobenius-degree-formula] relating the local
operator at a point to a power of the operator below it, and
$\mathcal K_\psi$ is of rank one with
eigenvalue $\lambda$ — and those of the second are
$\{\overline{\iota(\alpha)}^e\lambda^{-1}:\alpha\in E\}$ by Step 1.
Since conjugation of the complex numbers commutes with the $e$-th power,

$$
\overline{\iota(\alpha^e\lambda)}
=\overline{\iota(\alpha)}^e\,\overline{\iota(\lambda)}
=\overline{\iota(\alpha)}^e\lambda^{-1},
$$

the conjugation map carries the eigenvalue multiset of the first summand
bijectively onto that of the second, and the total multiset of
$\mathcal K$ at $z$ is conjugation-stable. Hence $\mathcal K$ is
$\iota$-real in the sense of [def-wf-iota-real], which is the
assertion of the lemma.
