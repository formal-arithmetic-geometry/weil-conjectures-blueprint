+++
id = "prose-04-03"
kind = "hidden"
title = "The base change map"
order = 174
+++
The coefficient ring is fixed after Definition [sk-def-pbc];
integral and rational coefficients are treated in Section [sec-pbc-condensed].
Results for abelian sheaves apply to sheaves of modules, because the
cohomology of a sheaf of $\Lambda$-modules agrees with the cohomology
of its underlying abelian sheaf [Stacks, Tag 03FD](https://stacks.math.columbia.edu/tag/03FD). The reason is that an
injective sheaf of modules is acyclic for the section functor on
every object of the site, although it need not be injective as an
abelian sheaf. Applying this on the étale objects over the target,
we get the same compatibility for $R^qu_*$ and, by bounded below
resolutions, for $Ru_*$.

Proper base change asserts that a specific map, from the pullback of the
direct image to the direct image of the pullback, is an isomorphism. We
define this map first, and describe it on sections so that we can compute
it on stalks. Consider a cartesian square

$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV @VV{f}V\\
Y' @>{g}>> Y.
\end{CD}
\tag{4.1}
$$

Since $gf'=fg'$, the composition isomorphisms of inverse images give
an isomorphism $f'^*g^*\simeq g'^*f^*$, on sheaves and, since inverse
images are exact, on bounded below derived categories. Let $F$ be a
sheaf on $X_{\acute{e}t}$. The *underived base change map*

$$
g^*f_*F\longrightarrow f'_*g'^*F
\tag{4.2}
$$

is the adjoint, under $f'^*\dashv f'_*$, of

$$
f'^*g^*f_*F
\simeq g'^*f^*f_*F
\xrightarrow{g'^*\varepsilon_f}g'^*F,
$$

where $\varepsilon_f:f^*f_*\to\mathrm{id}$ is the counit.
Equivalently, first apply the unit
$g^*f_*F\to f'_*f'^*g^*f_*F$, and then apply $f'_*$ to
the displayed composite. This construction is natural in $F$, and it applies
equally to sheaves of $\Lambda$-modules.

On sections the map has the following simple description. A section of $g^*f_*F$ over an
étale $V\to Y'$ is represented by an étale $W\to Y$, a map $V\to Y'\times_YW$, and a section over $X\times_YW$. The base change map restricts
this section along

$$
X'\times_{Y'}V\longrightarrow X\times_YW,
$$

and it is the sheafification of this map of presheaves.
