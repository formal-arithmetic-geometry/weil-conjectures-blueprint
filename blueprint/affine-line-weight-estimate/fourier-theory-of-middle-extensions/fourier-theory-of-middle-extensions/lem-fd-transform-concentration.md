+++
id = "lem-fd-transform-concentration"
kind = "lemma"
title = "The transform of a nonexceptional input is a sheaf; the Kiehl–Weissauer property (a)"
order = 4240
uses = ["def-fd-artin-schreier-sheaf", "def-fd-nonexceptional", "def-fd-transform", "def-wf-fundamental-representation", "lem-a1-affine-hc0", "lem-fd-fourier-concentration", "lem-fd-hc2-vanishing", "lem-fd-stalk-formula"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion with
$U_0=\mathbf A^1_{k_0}\setminus S_0$, and let $\mathcal M$ be an
irreducible lisse Weil sheaf on $U_0$ whose geometric fundamental
representation $V=\mathcal M_{\bar\eta}$ of
[def-wf-fundamental-representation] is irreducible, whose middle
extension is
Fourier-nonexceptional — so that $V$ is
in particular nontrivial — and which is unramified at infinity. Then for
every $a\in k$ the twisted compact-support cohomology of the input is
concentrated in degree one,

$$
H^q_c\bigl(\mathbf A^1_k,\,
j_!\mathcal M\otimes\mathcal L_{\psi(ax)}\bigr)=0
\qquad(q\neq1),
$$

and consequently the Fourier–Deligne transform
$\operatorname{FT}_\psi(j_!\mathcal M)$ of [def-fd-transform] is a
*sheaf*: its cohomology is concentrated in degree $0$. This is
property (a) of the Kiehl–Weissauer route recorded in
the extension-by-zero route, and it is the exactness half that upgrades the
amplitude bound of [thm-fd-fourier-perverse].

## Proof

For $a\neq0$ the vanishing of $H^0_c$ and of $H^2_c$ is exactly
[lem-fd-fourier-concentration], in the setting of
[def-fd-artin-schreier-sheaf]. For $a=0$ the group $H^0_c$
vanishes by [lem-a1-affine-hc0], and $H^2_c$ vanishes by
[lem-fd-hc2-vanishing], whose hypotheses are met because
$\mathcal M$ is irreducible with irreducible geometric representation and
is not geometrically constant, as
Fourier-nonexceptionality excludes the
constant sheaves. In both cases the twisted compact-support cohomology
is concentrated in degree one.

For the transform, let $\bar\xi$ be a geometric point of the dual line
$\mathbf A^1_k$ with $\xi\in k$. The stalk formula of
[lem-fd-stalk-formula] reads

$$
\bigl(\operatorname{FT}_\psi(j_!\mathcal M)\bigr)_{\bar\xi}
\cong H^*_c\bigl(\mathbf A^1_k,\,
j_!\mathcal M\otimes^L\mathcal L_{\psi(\xi x)}\bigr)[1]
=H^*_c\bigl(\mathbf A^1_k,\,
j_!\mathcal M\otimes\mathcal L_{\psi(\xi x)}\bigr)[1],
$$

and by the first part the right-hand side is concentrated in degree
$1-1=0$. This holds at every geometric point, so the transform is
concentrated in degree $0$, i.e. it is a sheaf.
