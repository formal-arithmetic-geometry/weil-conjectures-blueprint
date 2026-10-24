+++
kind = "proof"
of = "thm-fd-generic-fourier-sheaf-pure"
uses = ["cor-wf-unramified-boundary-purity", "def-wf-constant-weil-twist", "def-wf-determinantal-weight", "def-wf-iota-real", "def-wf-middle-extension", "fin2-lem-lisse-dense-open", "lem-a1-constituent-nonexceptional-comparison", "lem-fd-constituent-nonexceptional-concentration", "lem-fd-realified-kernel-real", "lem-fd-realness-pushforward", "lem-wf-constant-twist-cohomology", "lem-wf-constant-twist-weight", "prop-fd-zero-extension-comparison", "thm-rp-real-lisse-purity-affine"]
+++
*Step 0: twist to weight zero.* Since $\iota$ is only a field
embedding, $q^w$ need not lie in $\iota(\Qlb)$, so we first move
$\mathcal M$ to weight $0$, as in the construction of the real envelope.
Choose a closed point $x$ of $U_0$, of degree $d$, and an eigenvalue
$\alpha$ of $F_x$ on $\mathcal M_{\bar x}$; the stalk is nonzero because
$\mathcal M\neq0$ is lisse on the connected curve $U_0$, and
$\alpha\neq0$ because $F_x$ is an automorphism. Choose
$b\in\Qlb^\times$ with $b^d=\alpha^{-1}$. Purity gives
$|\iota(b)|=|\iota(\alpha)|^{-1/d}=q^{-w/2}$, that is
$2\log_q|\iota(b)|=-w$, so by [lem-wf-constant-twist-weight] the
constant twist ([def-wf-constant-weil-twist])

$$
\mathcal M^0:=\mathcal M\otimes\mathcal B_b
$$

is punctually $\iota$-pure of weight $0$. It is again a nonzero
irreducible lisse Weil sheaf on $U_0$ which is constituent-nonexceptional:
apply [lem-fd-constituent-nonexceptional-concentration](2) first to
$\mathcal M$ with $b^{-1}$ and then to
$\mathcal M^\vee\otimes\mathcal B_{b^{-1}}$ with $1$, and use
$\mathcal M^{\vee\vee}\cong\mathcal M$ and
$\mathcal B_{b^{-1}}^\vee\cong\mathcal B_b$.

*Step 1: the real envelope after zero extension.* Let $\mathcal K$ be
the realified kernel on the Fourier square formed as in
[lem-fd-realified-kernel-real] from $\mathcal M^0$, of weight $0$, with
the constant $1$ (indeed $\iota(1)=1=q^0$), so that
$(\mathcal M^0)^\dagger=(\mathcal M^0)^\vee\otimes\mathcal B_1
=(\mathcal M^0)^\vee$. By the general form of
[lem-fd-realified-kernel-real], which needs only the purity of
$\mathcal M^0$, the constructible Weil sheaf $\mathcal K$ is
$\iota$-real. By [lem-fd-constituent-nonexceptional-concentration](3),
applied to $\mathcal M^0$,
$R^\nu p_{2,!}\mathcal K=0$ for $\nu\neq1$, and the sheaf

$$
\mathcal G^0:=\operatorname{FT}_\psi(j_!\mathcal M^0)
$$

(concentrated in degree $0$) is a direct summand of
$\mathcal H:=R^1p_{2,!}\mathcal K$. By [lem-fd-realness-pushforward],
applied to $\mathcal K$ and this vanishing, $\mathcal H$ is an
$\iota$-real constructible Weil sheaf on the dual line $A'_0$. Working
with $j_!\mathcal M^0$ rather than $j_*\mathcal M^0$ is what makes the
reality available: at a missing point both summands of $\mathcal K$ have
zero stalk, while the boundary stalks of $j_*\mathcal M^0$ and
$j_*(\mathcal M^0)^\vee$ need not have conjugate spectra.

*Step 2: $\mathcal G^0$ surjects onto the twisted middle extension.* By
the zero-extension comparison [prop-fd-zero-extension-comparison], whose
hypotheses are exactly those of the present statement, the sheaf
$\mathcal G:=\operatorname{FT}_\psi(j_!\mathcal M)$ satisfies
$\operatorname{FT}_\psi(j_!\mathcal M[1])\cong\mathcal G[1]$ and there is
a short exact sequence of Weil sheaves
$0\to\mathcal B'\to\mathcal G\to j'_*\mathcal M'\to0$ on the dual line,
with $j'_*\mathcal M'$ the middle extension of
[def-wf-middle-extension]. The constant twist $\mathcal B_b$ has the
constant underlying sheaf and only rescales Weil structures, so
$j_!(\mathcal M\otimes\mathcal B_b)=(j_!\mathcal M)\otimes\mathcal B_b$,
both $p_1^*\mathcal B_b$ and $p_2^*\mathcal B_b$ are the constant twist
$\mathcal B_b$ of the Fourier square, and tensoring with $\mathcal B_b$
is exact. The projection formula [lem-wf-constant-twist-cohomology] for
$h=p_2$ therefore gives $\mathcal G^0\cong\mathcal G\otimes\mathcal B_b$,
and $\mathcal G^0\to(j'_*\mathcal M')\otimes\mathcal B_b$ is an
epimorphism of Weil sheaves.

*Step 3: purity on a dense open.* By [fin2-lem-lisse-dense-open],
applied to $\mathcal H$ and to $\mathcal G^0$ and intersected with
$U'_0$, there is a dense open $V'_0\subset U'_0$ on which $\mathcal H$
and $\mathcal G^0$ are lisse. Restriction to $V'_0$ is exact and additive,
and $(j'_*\mathcal M')|_{V'_0}=\mathcal M'|_{V'_0}$. Composing the
projection $\mathcal H\to\mathcal G^0$ onto the direct summand with the
epimorphism of Step 2 gives an epimorphism of lisse Weil sheaves

$$
\mathcal H|_{V'_0}\twoheadrightarrow(\mathcal M'\otimes\mathcal B_b)|_{V'_0}.
$$

The restriction $\mathcal M'|_{V'_0}$ is nonzero and irreducible: the
Weil group of the dense open $V'_0$ of the normal connected curve
$U'_0$ surjects onto that of $U'_0$ (the corresponding surjectivity of
étale fundamental groups for a dense open of a normal connected scheme,
SGA 1, Exp. V, 8.2), so the invariant subspaces are the same. Twisting
the representation by the character through which $\mathcal B_b$ acts
does not change the invariant subspaces, so
$(\mathcal M'\otimes\mathcal B_b)|_{V'_0}$ is nonzero and irreducible as
well. Refining the kernel of this epimorphism to a composition series of
$\mathcal H|_{V'_0}$ shows that $(\mathcal M'\otimes\mathcal B_b)|_{V'_0}$
is an irreducible constituent of $\mathcal H|_{V'_0}$, which is lisse
and $\iota$-real ([def-wf-iota-real]; reality is a pointwise condition
and passes to the open). As $V'_0$ is a dense open of the affine line,
it is a smooth geometrically connected affine curve, and
[thm-rp-real-lisse-purity-affine] shows that
$(\mathcal M'\otimes\mathcal B_b)|_{V'_0}$ is punctually $\iota$-pure of
the real weight
$v_0:=\dw_\iota\bigl((\mathcal M'\otimes\mathcal B_b)|_{V'_0}\bigr)$, its
determinantal weight of [def-wf-determinantal-weight]. Untwisting,
$\mathcal M'|_{V'_0}\cong(\mathcal M'\otimes\mathcal B_b)|_{V'_0}\otimes
\mathcal B_{b^{-1}}$ with $2\log_q|\iota(b^{-1})|=w$, so by
[lem-wf-constant-twist-weight] the sheaf $\mathcal M'|_{V'_0}$ is
punctually $\iota$-pure of the real weight $v:=v_0+w$.

*Step 4: purity on all of $U'_0$.* The sheaf $\mathcal M'$ is lisse on
the smooth geometrically connected curve $U'_0$ and its restriction to
the dense open $V'_0$ is punctually $\iota$-pure of weight $v$. At a
point $x\in U'_0\setminus V'_0$ the inertia acts trivially, $\mathcal M'$
being lisse there, and the ordinary direct image from $V'_0$ recovers the
stalk of $\mathcal M'$ (the translation step of
[lem-a1-constituent-nonexceptional-comparison]). The consequence
clause of [cor-wf-unramified-boundary-purity] therefore gives that
$\mathcal M'$ is punctually $\iota$-pure of weight $v$ on all of
$U'_0$.
