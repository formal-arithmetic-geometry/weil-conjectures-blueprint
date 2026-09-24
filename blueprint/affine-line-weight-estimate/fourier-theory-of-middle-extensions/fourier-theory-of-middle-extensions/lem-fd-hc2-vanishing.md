+++
id = "lem-fd-hc2-vanishing"
kind = "lemma"
title = "Vanishing of the top compact-support group of the input"
order = 4237
uses = ["def-fd-nonexceptional", "def-weil-ordinary-compact-cohomology", "def-wf-fundamental-representation", "lem-a1-affine-hc2"]
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

The middle extension $j_*\mathcal M$ differs from $j_!\mathcal M$ by
the extension by zero of the restriction to the finite set $S_0$,
which is zero-dimensional: $H_c^q(\mathbf A^1,i_*B)=H^q(S_0,B)=0$ for
$q\ge1$ because $S_0$ has dimension zero. Hence

$$
H_c^2\bigl(\mathbf A^1_{k_0},j_*\mathcal M\bigr)
=H_c^2\bigl(\mathbf A^1_{k_0},j_!\mathcal M\bigr)
=H_c^2(U,\mathcal M),
$$

the last group being taken on the affine curve $U$. The description
of the top group on an affine curve [lem-a1-affine-hc2] identifies
it with the Tate twist of the coinvariants of the geometric monodromy
action of [def-wf-fundamental-representation],

$$
H_c^2(U,\mathcal M)\cong V_{\pi_1(U)}(-1).
$$

It remains to see that those coinvariants vanish. A
$\pi_1(U)$-invariant functional on $V$ is an element of the
invariant space $(V^\vee)^{\pi_1(U)}$, which is nonzero only if
$V^\vee$ admits the trivial module as a subquotient, hence — $V^\vee$
being irreducible — only if $V^\vee$ is the trivial module, that is,
only if $V$ is. But $V$ is irreducible and nontrivial: irreducibility
is a hypothesis, and nontriviality holds because a geometrically
constant irreducible lisse sheaf is a constant sheaf up to a constant
Weil twist, which
Fourier-nonexceptionality excludes.
Therefore $V_{\pi_1(U)}=0$ and
$H_c^2(\mathbf A^1_{k_0},j_*\mathcal M)=0$.
