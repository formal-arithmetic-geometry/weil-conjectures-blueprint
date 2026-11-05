+++
id = "prose-E-29"
kind = "hidden"
title = "Contracting correspondences (4)"
order = 1705
+++
The proof of the main theorem combines the two lemmas on the
deformation with Verdier's theorem and with the specialization of trace
classes. The statement of the main theorem involves the restriction of a correspondence to
$Z$, which we construct first.

Let $c=(c_1,c_2):C\to X\times X$ be a correspondence, let
$Z\hookrightarrow X$ have ideal $I$, and suppose that
$c_2^{-1}(I)\mathcal O_C\subset c_1^{-1}(I)\mathcal O_C$. Then
$c_1^{-1}(Z)\subset c_2^{-1}(Z)$. As before
Lemma [lemma-lift-correspondence-invariant-decomposition], we put

$$
C_Z=(c_1^{-1}Z)_{\mathrm{red}},\qquad
c_Z=(c_{Z,1},c_{Z,2}):C_Z\longrightarrow Z_{\mathrm{red}}\times Z_{\mathrm{red}},
$$

with $i:Z_{\mathrm{red}}\hookrightarrow X$ and
$i':C_Z\hookrightarrow C$. For $K\in D^b_{\mathrm{ctf}}(X,A)$ put $K_Z=i^*K$. The
square formed by $i'$, $i$, $c_1$ and $c_{Z,1}$ is cartesian up to
reduction. Hence invariance under nilpotent thickenings and base
change for direct image with compact support give
$i^*Rc_{1!}\simeq Rc_{Z,1!}i'^*$. Since the second leg maps $C_Z$ into
$Z_{\mathrm{red}}$, we also have $i'^*c_2^*K\simeq c_{Z,2}^*K_Z$. For a
cohomological correspondence $u:c_2^*K\to c_1^!K$ with adjoint
$\widehat u:Rc_{1!}c_2^*K\to K$ under $Rc_{1!}\dashv c_1^!$, the
*restriction* $u_Z:c_{Z,2}^*K_Z\to c_{Z,1}^!K_Z$ of $u$ to $Z$ is the
adjoint under $Rc_{Z,1!}\dashv c_{Z,1}^!$ of

$$
Rc_{Z,1!}c_{Z,2}^*K_Z
\simeq i^*Rc_{1!}c_2^*K
\xrightarrow{i^*\widehat u}K_Z.
\tag{E.21}
$$

Equivalently, $u_Z$ is $i'^*u$ followed by the base change map
$i'^*c_1^!K\to c_{Z,1}^!K_Z$, which in general is not an
isomorphism. This is the restriction to $Z$ that occurs in
Lemma [lemma-closed-piece-pushforward]. If $F_0$ is an open and
closed subscheme of $\Fix(c)$, put $F_{0,Z}=\Fix(c_Z)\times_{\Fix(c)}F_0$,
and let $h_{F_0}:F_{0,Z}\to F_0$ be the projection.
