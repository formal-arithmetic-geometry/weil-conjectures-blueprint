+++
kind = "proof"
of = "sk-lem-pd-generic-restriction"
uses = ["sk-prop-ctf-finite-comparison", "sk-lem-pd-preservation"]
+++
The comparisons are proved in the order stated, each from the
previous ones: direct image by continuity along a limit of étale
maps, $i^!$ by the localization triangle, internal Hom by
dévissage to generators $t_!P$, and the twist by a closed embedding
into affine space.

By [sk-prop-ctf-finite-comparison], with finite coefficients
$\Dctf(X,A)$ and the direct images are computed by their classical
étale counterparts. A separable closure of
$k(B)$ is the inverse limit of nonempty affine opens in the
normalizations of $B$ in its finite separable extensions, with
the branch loci removed. Each stage is étale over an open of
$B$. Smooth base change (the section on smooth base change)
commutes $Rh_*$ with these stagewise pullbacks. Every affine object
étale over the limit descends to a stage. Continuity of
finite-coefficient étale cohomology for affine transition maps
then commutes their derived sections, degree by degree, with this
filtered limit. Thus the first comparison passes to the separable
closure. A purely inseparable extension induces the same classical
étale topos, so passage to the algebraic closure gives the asserted
comparison. The argument uses the comparison for bounded-below
complexes and a bound on $\operatorname{cd}_\ell$ holding
uniformly over the stages. This is [det-pd-generic-direct-image].

For the second comparison, let $j$ be the open complement of
$i$ and pull back

$$
 i_*i^!M\longrightarrow M\longrightarrow Rj_*j^*M
 \longrightarrow.
$$

The first comparison treats $Rj_*$; pullback commutes with closed
direct image. The pulled-back triangle is therefore the closed-support
triangle on the generic fibre. Full faithfulness of
$i_{\bar\eta,*}$ identifies the fibres and proves the second
comparison.

For internal Hom, reduce its first variable by the finite smooth
stratification to $K=t_!P$, where $t$ is the inclusion of a
stratum and $P$ is locally perfect on it. Then

$$
 \cHom_X(t_!P,M)
 \simeq Rt_*(P^\vee\otimes^{\mathbf L}t^!M).
$$

The first two comparisons, a factorization of $t$ into an open
and a closed immersion, and dualizability of $P$ prove the claim
on these generators; finite cones prove it for $K$. All complexes
used remain bounded constructible by [sk-lem-pd-preservation].
The second and third comparisons are [det-pd-generic-closed-hom].

Finally, on an affine open of $X$ choose a closed immersion over
$\mathbf A^1_k$ into $\mathbf A^r_{\mathbf A^1_k}$.
Composition and smooth purity compute its dualizing complex as
$i^!A(r+1)[2r+2]$, whereas that of the geometric generic fibre
is $i_{\bar\eta}^!A(r)[2r]$. The closed-support comparison gives
the displayed twist. All comparisons were formed from localization,
pullback and adjunction, so they preserve evaluation. Applying the
internal-Hom comparison twice cancels the twist and shift and gives
the assertion about $\delta$; see [det-pd-generic-dualizing-twist].
