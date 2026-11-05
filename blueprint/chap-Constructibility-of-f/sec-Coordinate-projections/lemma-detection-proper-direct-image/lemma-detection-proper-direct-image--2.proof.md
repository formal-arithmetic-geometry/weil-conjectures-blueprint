+++
kind = "proof"
of = "lemma-detection-proper-direct-image--2"
order = 569005
uses = ["lemma-finite-morphisms", "proposition-extension-zero-restriction-closed-subscheme--8"]
+++
Complete $\varphi$ to a distinguished triangle
$K\to K'\to M\to K[1]$. Applying $j^*$ and $Rb_*$ shows that
$j^*M=0$ and $Rb_*M=0$.

The étale open–closed triangle, the derived form of
[proposition-extension-zero-restriction-closed-subscheme--8], is

$$
j_!j^*M\longrightarrow M\longrightarrow Ri_*i^*M
\longrightarrow j_!j^*M[1].
$$

Its first term vanishes, so the unit $M\to Ri_*i^*M$ is an isomorphism.
Put $N=i^*M$. Composition of derived direct images then gives

$$
R(bi)_*N\simeq Rb_*Ri_*N\simeq Rb_*M=0.
$$

Since $bi$ is finite, its direct image is exact by
[lemma-finite-morphisms]. Hence $(bi)_*H^n(N)=0$ for every $n$.
The finite stalk formula shows that a zero direct image forces every
stalk of $H^n(N)$ to vanish: each such stalk is a factor of the finite
product over its image in $S$. This is
`AlgebraicGeometry.Etale.isZero_of_isZero_lowerStar_obj_of_isFinite`.
Thus all cohomology sheaves of $N$ vanish, and $N=0$ by
`AlgebraicGeometry.Etale.isZero_of_forall_isZero_homology`.
It follows that $M=0$, so $\varphi$ is an isomorphism.
