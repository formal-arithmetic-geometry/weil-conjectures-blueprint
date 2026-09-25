+++
id = "lem-fd-nonexceptional-dual"
kind = "lemma"
title = "The dual twist of a nonexceptional input is nonexceptional"
order = 2949
uses = ["def-fd-nonexceptional", "def-weil-pbc-constructible-complexes", "def-wf-constant-weil-twist", "def-wf-fundamental-representation", "def-wf-middle-extension", "lem-fd-as-characters", "lem-fd-transform-concentration"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion and
let $\mathcal M$ be an irreducible
lisse Weil sheaf on
$U_0$ which is unramified at infinity, whose geometric fundamental
representation $V=\mathcal M_{\bar\eta}$ of
[def-wf-fundamental-representation] is irreducible, and whose
middle extension is
Fourier-nonexceptional. Fix
$b\in\Qlb^\times$ and put

$$
\mathcal M^\dagger:=\mathcal M^\vee\otimes\mathcal B_b,
$$

the linear dual twisted by the constant
Weil twist of
[def-wf-constant-weil-twist]. Then $\mathcal M^\dagger$ is lisse and
irreducible on $U_0$, unramified at infinity, its geometric fundamental
representation $V^\vee\otimes\chi_b$ is irreducible, and its middle
extension is again Fourier-nonexceptional.

## Proof

Lissity and the irreducible geometric representation are elementary
linear algebra over the coefficient field: the dual of an irreducible
module is irreducible, and tensoring an irreducible module with a
one-dimensional module preserves irreducibility (if
$W\subseteq V^\vee\otimes\chi_b$ is nonzero then
$W\otimes\chi_b^{-1}$ is a nonzero submodule of $V^\vee$). Lissity of
the dual and of the tensor product is the lisse convention of
[def-weil-pbc-constructible-complexes], and
$V^\vee\otimes\chi_b$ is nontrivial because $V$ is.
Irreducibility of $\mathcal M^\dagger$ as a Weil sheaf is the same
statement with the arithmetic structure, the constant twist acting by a
character of $\pi_1(U_0)$.

Unramifiedness at infinity is preserved: the local monodromy
representation at a boundary point of $\mathcal M^\vee$ is the dual of
the local monodromy of $\mathcal M$, which is trivial when the latter is,
and the constant Weil twist is lisse on all of $\mathbf A^1_{k_0}$.

It remains to test Fourier-nonexceptionality, and by
[def-fd-nonexceptional] this is a condition after geometric base
change, i.e. a condition on the lisse sheaf $\mathcal M_{\bar k}$ on
$U_{\bar k}$: it must be neither constant nor the restriction of an
Artin–Schreier sheaf $\mathcal L_{\psi(ax)}$. After geometric base
change the twist $\mathcal B_b$ becomes the constant sheaf, so
$\mathcal M^\dagger_{\bar k}=(\mathcal M_{\bar k})^\vee$. If
$(\mathcal M_{\bar k})^\vee$ were constant then so would be
$\mathcal M_{\bar k}=((\mathcal M_{\bar k})^\vee)^\vee$, which is
excluded. If $(\mathcal M_{\bar k})^\vee\cong \mathcal L_{\psi(ax)}|_{U_{\bar k}}$ then inverting the rank-one lisse
sheaf, using $(\mathcal L_{\psi,ax})^{-1}\cong\mathcal L_{-\psi,ax}$ of
[lem-fd-as-characters] and
$\mathcal L_{-\psi,ax}=\mathcal L_{\psi(-a)x}$, gives
$\mathcal M_{\bar k}\cong\mathcal L_{\psi(-a)x}|_{U_{\bar k}}$, which is
excluded as well.

The hypothesis list of [lem-fd-transform-concentration] is thereby
met: it asks for an irreducible lisse input with irreducible geometric
fundamental representation, unramified at infinity, with
Fourier-nonexceptional middle extension, and its statement involves the
additive character only through the kernel.
