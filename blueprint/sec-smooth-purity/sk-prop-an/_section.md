+++
id = "sk-prop-an"
kind = "section"
title = "$\\Aaf^1\\Rightarrow\\Aaf^n$: the model purity"
order = 2039
uses = ["sk-def-purity-conv", "sk-prop-a1", "sk-prop-a1-inv"]
+++
*Proposition (sketch).*

In the conventions of [sk-def-purity-conv], let $B$ be separated finite
type and $z:B\hookrightarrow\Aaf^c_B$ the zero section. Then

$$
Rz^{!}\Lambda_{\Aaf^c_B}(c)[2c]\ \cong\ \Lambda_B,
$$

i.e. $Rz^{!}\Lambda_{\Aaf^c_B}\cong\Lambda_B(-c)[-2c]$, by a canonical
base-change compatible isomorphism whose generator is the fundamental class
of the zero section. More generally, for a vector bundle $\pi:E\to Z$ of
rank $c$ with zero section $z$ there is a *Thom class*

$$
\mathrm{th}_E:\ \Lambda_Z\ \xrightarrow{\ \sim\ }\ Rz^{!}\Lambda_E(c)[2c],
$$

which restricts to the previous one in any étale trivialization of $E$.

## Proof

*Step 1: the model case.* Write
$\Aaf^c_B=\Aaf^1_B\times_B\cdots\times_B\Aaf^1_B$ and $z=s\times_B\cdots\times_Bs$.
Künneth for cohomology with supports gives

$$
Rz^{!}\bigl(K_1\boxtimes_B\cdots\boxtimes_BK_c\bigr)
\ \simeq\ Rs^{!}K_1\otimes^{\mathrm L}\cdots\otimes^{\mathrm L}Rs^{!}K_c ,
$$

the case $c=2$ iterated. Take $K_i=\Lambda_{\Aaf^1_B}(1)[2]$ and use
$\Lambda(c)[2c]=(\Lambda(1)[2])^{\otimes c}$: by [sk-prop-a1] each factor
is $\Lambda_B$, so $Rz^{!}\Lambda_{\Aaf^c_B}(c)[2c]\cong\Lambda_B$, with
canonical generator $\mathrm{pur}_s\otimes\cdots\otimes\mathrm{pur}_s$, the
boundary of $\kappa(t_1)\cup\cdots\cup\kappa(t_c)$.

*Step 2: the sheaf of orientations.* Let $\pi:E\to Z$ have rank $c$ and
choose an étale cover $\{U_\alpha\to Z\}$ trivializing $E$. Formation of
$Rz^{!}$ commutes with the base changes involved, so by Step 1 the complex
$Rz^{!}\Lambda_E(c)[2c]$ restricted to each $U_\alpha$ is concentrated in
degree zero with $\mathcal H^0$ free of rank one. Hence
$\mathcal L_E:=\mathcal H^0\bigl(Rz^{!}\Lambda_E(c)[2c]\bigr)$ is a lisse
rank-one sheaf on $Z$, and giving $\mathrm{th}_E$ amounts to giving a global
section of $\mathcal L_E$ generating every stalk. This is the mechanism
inherited from [sk-prop-a1]: what is glued below are *sections of a
lisse sheaf on $Z_{\Et}$*, for which the sheaf axiom suffices, not objects or
morphisms of $D^b$, for which étale descent is unavailable in the ordinary
derived category.

*Step 3: independence of the frame.* On $U_\alpha$ a frame
$f_1,\dots,f_c$ of the ideal of the zero section gives the section
$\partial(\kappa(f_1)\cup\cdots\cup\kappa(f_c))$ of Step 1. Two frames
differ by some $g\in GL_c(\mathcal O(U_\alpha))$, and after refining the cover
$g$ is a product of diagonal, permutation and elementary matrices; the
section is unchanged under each. Diagonal:
$\kappa(uf_i)=\kappa(u)+\kappa(f_i)$ and $\kappa(u)$ extends across the zero
locus, so it dies under the boundary. Permutation: each $\kappa(f_i)$
contributes total degree $2$, so a transposition carries sign $+1$.
Elementary: the family $f(t)$ over $\Aaf^1_{U_\alpha}$ gives a section of a
lisse sheaf on the line, constant along it by [sk-prop-a1-inv] (i), so the
classes at $t=0$ and $t=1$ agree.

*Step 4: gluing.* By Step 3 the local sections of Step 1 agree on
overlaps, so by the sheaf axiom for $\mathcal L_E$ they glue to a unique
global section $\mathrm{th}_E$, generating every stalk. A generating section
of a lisse rank-one sheaf is an isomorphism, which is the assertion. Base-change
compatibility is inherited from [sk-prop-a1].

Uses: [sk-def-purity-conv], [sk-prop-a1-inv], [sk-prop-a1]
