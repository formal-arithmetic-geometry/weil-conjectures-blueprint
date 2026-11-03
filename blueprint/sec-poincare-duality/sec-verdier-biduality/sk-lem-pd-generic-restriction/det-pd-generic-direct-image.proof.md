+++
kind = "proof"
of = "det-pd-generic-direct-image"
uses = ["sbc-thm-bounded-below-derived-smooth-base-change", "lem-weil-pbc-derived-cohomology-continuity", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
*Separable closure.* Let $k(B)^{\mathrm{sep}}\subseteq\overline{k(B)}$ be the
separable closure. It is the inverse limit of nonempty affine opens
$B_\alpha$ in the normalizations of $B$ in its finite separable extensions,
with the branch loci removed. Each $B_\alpha$ is étale over an open of $B$, and
the transition maps are affine. Write $T_\alpha=T\times_BB_\alpha$ and
$X_\alpha=X\times_BB_\alpha$. Since $X_\alpha\to X$ is étale, hence smooth,
bounded-below smooth base change
([sbc-thm-bounded-below-derived-smooth-base-change]) commutes $Rh_*$ with
pullback to each stage: $(Rh_*L)|_{X_\alpha}\simeq Rh_{\alpha,*}(L|_{T_\alpha})$.

*Passage to the limit.* Let $X^{\mathrm{sep}}=\varprojlim_\alpha X_\alpha$ and
$T^{\mathrm{sep}}=\varprojlim_\alpha T_\alpha$. Every affine object étale over
$X^{\mathrm{sep}}$ descends to an affine object $V_\alpha$ étale over some
$X_\alpha$, and its preimage in $T^{\mathrm{sep}}$ is the limit of the preimages
of the $V_\beta=V_\alpha\times_{X_\alpha}X_\beta$ in $T_\beta$, $\beta\geq\alpha$.
Continuity of finite-coefficient étale cohomology for affine transition maps
([lem-weil-pbc-derived-cohomology-continuity]) identifies, degree by degree,
the cohomology of $L$ on this preimage with the filtered colimit of the
stagewise cohomology groups, which compute the sections of $Rh_{\beta,*}$ on
$V_\beta$. The same continuity applied to $Rh_*L$ on $X$ computes the sections
of its pullback on the descended object. By the previous step these two
colimits agree, so the comparison holds over $\operatorname{Spec}k(B)^{\mathrm{sep}}$.
The argument uses the comparison for bounded-below complexes and a bound on
$\operatorname{cd}_\ell$ holding uniformly over the stages, so that the degree
by degree identification determines the complexes.

*Algebraic closure.* The extension $\overline{k(B)}/k(B)^{\mathrm{sep}}$ is
purely inseparable. Its base changes $X_{\bar\eta}\to X^{\mathrm{sep}}$ and
$T_{\bar\eta}\to T^{\mathrm{sep}}$ are universal homeomorphisms, so they induce
equivalences of étale topoi compatible with direct and inverse images and with
cohomology ([thm-weil-pbc-universal-homeomorphism-invariance]). This gives the
comparison over $\bar\eta$.
