+++
kind = "proof"
of = "lemma-largest-punctual-subsheaf--1"
uses = ["proposition-topos-functoriality", "proposition-pro-etale-coverings", "definition-lisse-sheaves"]
+++
Remove the finite support of $G$ to obtain an open $V_0$ on which $G$
vanishes. After passing to the geometric fibre, the generic point of
$\Aone_{\overline{k}_0}$ lies over $V_0$: otherwise its image would be a
closed point specializing to every point of the affine line, which is
impossible. Every point of $U=U_0\times_{k_0}\overline{k}_0$ therefore
specializes from a point of $U\cap V$, where
$V=V_0\times_{k_0}\overline{k}_0$.

The morphism $G\to j_*M$ is adjoint, on the underlying pro-étale sheaves,
to a morphism $j^*G\to M$ which vanishes on $U\cap V$. A morphism into a
lisse sheaf which vanishes on such an open vanishes everywhere
(`AlgebraicGeometry.ProEtale.IsAdicLisseSheaf.eq_zero_of_adicUpperStar_map_eq_zero`).
Indeed, on a pro-étale cover trivializing the target, reduce to its
$\overline{\mathbf Q}_\ell$-valued components. Weakly étale maps lift
generizations, and a continuous function into the Hausdorff field
$\overline{\mathbf Q}_\ell$ is constant along specializations. Each
component is thus zero. Adjunction gives the desired vanishing, and a
zero monomorphism has zero source.
