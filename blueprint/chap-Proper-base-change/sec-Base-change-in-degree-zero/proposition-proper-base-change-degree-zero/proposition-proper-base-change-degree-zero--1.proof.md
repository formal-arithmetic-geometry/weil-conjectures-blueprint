+++
kind = "proof"
of = "proposition-proper-base-change-degree-zero--1"
order = 334002
uses = ["lemma-sections-geometric-fibre", "definition-underived-base-change-map"]
+++
Put $\bar y=g\bar y'$ and $Z=X'\times_{Y'}\operatorname{Spec}\Omega$,
and write $a':Z\to X'$ for the projection. Pasting cartesian squares
identifies $Z$ with $X\times_Y\operatorname{Spec}\Omega$, with projection
$a=g'a'$ to $X$. Properness is preserved by base change, so
[lemma-sections-geometric-fibre] gives bijections

$$
\zeta:(f_*F)_{\bar y}\longrightarrow\Gamma(Z,a^*F),\qquad
\zeta':(f'_*g'^*F)_{\bar y'}\longrightarrow\Gamma(Z,a'^*g'^*F).
$$

The stalk of an inverse image gives an isomorphism
$e:(g^*f_*F)_{\bar y'}\xrightarrow{\sim}(f_*F)_{\bar y}$, and
composition of inverse images gives an isomorphism
$c:\Gamma(Z,a'^*g'^*F)\xrightarrow{\sim}\Gamma(Z,a^*F)$.
If $\beta$ denotes the map in the statement, we claim that

$$
c\circ\zeta'\circ\beta=\zeta\circ e.
$$

To check this equality, represent a germ by a section over an étale
neighbourhood of $\bar y'$. After refining the neighbourhood, the section
is the pullback of a section of $f_*F$ over an étale neighbourhood in
$Y$. Since $\Omega$ is algebraically closed, the geometric point lifts
to this refinement. By the formula for
[definition-underived-base-change-map] on pulled back sections, its
image is the pullback along the induced map between the two base changes
of these neighbourhoods. Restricting to $Z$ therefore gives the same
section as first applying $e$ and then $\zeta$; the isomorphism $c$
identifies the two iterated inverse images. This proves the equality.
Since $c$, $\zeta'$, $\zeta$, and $e$ are bijective, so is $\beta$.
