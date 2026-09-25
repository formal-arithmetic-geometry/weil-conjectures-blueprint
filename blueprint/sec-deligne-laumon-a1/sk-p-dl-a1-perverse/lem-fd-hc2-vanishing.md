+++
id = "lem-fd-hc2-vanishing"
kind = "lemma"
title = "Vanishing of the top compact-support group of the input"
order = 2994
uses = ["def-fd-nonexceptional", "def-weil-ordinary-compact-cohomology", "def-wf-fundamental-representation", "lem-a1-middle-extension-endpoints"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion
with $U_0=\mathbf A^1_{k_0}\setminus S_0$, and let $\mathcal M$ be an
irreducible lisse Weil sheaf on $U_0$ whose geometric fundamental
representation $V=\mathcal M_{\bar\eta}$ of
[def-wf-fundamental-representation] is irreducible, and which is
*not geometrically constant* — as is the case for a
Fourier-nonexceptional middle
extension. Then, in the compactly supported cohomology of
[def-weil-ordinary-compact-cohomology],

$$
H_c^2\bigl(\mathbf A^1_{k_0},\,j_*\mathcal M\bigr)=0 .
$$

## Proof

The affine line is a smooth geometrically connected affine curve, so
the endpoint lemma [lem-a1-middle-extension-endpoints], applied with
$C_0=\mathbf A^1_{k_0}$, identifies the top group with the Tate twist
of the coinvariants of the geometric monodromy action of
[def-wf-fundamental-representation],

$$
H_c^2\bigl(\mathbf A^1_{k_0},j_*\mathcal M\bigr)\cong V_{\pi_1(U)}(-1).
$$

It remains to see that those coinvariants vanish. A
$\pi_1(U)$-invariant functional on $V$ is an element of the
invariant space $(V^\vee)^{\pi_1(U)}$, which is nonzero only if
$V^\vee$ admits the trivial module as a subquotient, hence — $V^\vee$
being irreducible — only if $V^\vee$ is the trivial module, that is,
only if $V$ is. But $V$ is irreducible and nontrivial: irreducibility
is a hypothesis, and nontriviality holds because a trivial $V$ means
that $\pi_1(U)$ acts trivially, i.e. that $\mathcal M$ is geometrically
constant, which is excluded by hypothesis (and by
Fourier-nonexceptionality).
Therefore $V_{\pi_1(U)}=0$ and
$H_c^2(\mathbf A^1_{k_0},j_*\mathcal M)=0$.
