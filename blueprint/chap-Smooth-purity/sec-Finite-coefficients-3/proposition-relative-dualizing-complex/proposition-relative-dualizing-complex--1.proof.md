+++
kind = "proof"
of = "proposition-relative-dualizing-complex--1"
order = 755002
uses = ["lemma-affine-space-etale-localization", "proposition-purity-vector-bundles", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-composition-open-restriction-compactifications-f"]
+++
Put $T=\Lambda_V(d)[2d]$. Locally along $s(S)$, choose étale coordinates
$x_1,\ldots,x_d$ cutting out the section. The product of their Kummer
boundary classes is the restriction of the Thom class of the zero
section of affine space. Its adjoint is an isomorphism by affine-space
purity and étale localization
([proposition-purity-vector-bundles], [lemma-affine-space-etale-localization]).
The coordinates form a regular sequence, and the frame classes agree on
overlaps and glue uniquely to a fundamental class of $s$. Its adjoint
$\Lambda_S\to Rs^!T$ is an isomorphism, as can be checked on these
frames. Write $\theta:Rs^!T\xrightarrow{\sim}\Lambda_S$ for its inverse.

Since $g\circ s=\operatorname{id}_S$, composition for the exceptional
inverse image [proposition-composition-open-restriction-compactifications-f]
gives $\varepsilon:Rs^!\omega_g\xrightarrow{\sim}\Lambda_S$.
Both $T$ and $\omega_g$ are invertible for the derived tensor product;
for $\omega_g$ this is
[proposition-exceptional-inverse-image-smooth-morphism](1).
The tensor map
$Rs^!M\otimes^{\mathbf L}Ls^*N\to Rs^!(M\otimes^{\mathbf L}N)$,
obtained from the projection formula by adjunction, is an isomorphism
when $N$ is invertible. Using it twice and the symmetry of the tensor
product gives

$$
\begin{aligned}
Ls^*\omega_g
&\simeq Rs^!T\otimes^{\mathbf L}Ls^*\omega_g
\simeq Rs^!(T\otimes^{\mathbf L}\omega_g)\\
&\simeq Rs^!(\omega_g\otimes^{\mathbf L}T)
\simeq Rs^!\omega_g\otimes^{\mathbf L}Ls^*T
\simeq Ls^*T
\simeq\Lambda_S(d)[2d].
\end{aligned}
$$

Here the first and penultimate isomorphisms use $\theta$ and
$\varepsilon$, and the last uses pullback of the Tate twist. The
fundamental class is determined by the fixed Kummer class and its
restrictions to the coordinate frames, so this composite is canonical.
