+++
kind = "proof"
of = "sk-cor-geo-open-finiteness"
uses = ["sk-thm-geo-generic-open", "sk-thm-pe-direct-image-comparison", "sk-thm-pe-constructible-comparison"]
+++
We argue on the étale site; bounded constructible and direct-image comparison
([sk-thm-pe-constructible-comparison], [sk-thm-pe-direct-image-comparison])
identify the result and its base-change maps with the asserted pro-étale ones.

For a constructible $\Fell$-sheaf this is [sk-thm-geo-generic-open] with
$S=\operatorname{Spec}k$: the only nonempty open of $\operatorname{Spec}k$ is
itself, so the theorem gives a statement with no shrinking. A constructible
sheaf killed by $\ell^r$ has a finite filtration by the images of
multiplication by powers of $\ell$, with constructible $\Fell$-sheaves as
successive quotients; the long exact cohomology sequences give (G25), and
morphisms between the resulting triangles give the base-change assertion. For a
finite $\ell$-primary ring $\Lambda$, apply this to the underlying
$\mathbf Z/\ell^r\mathbf Z$-sheaf, carrying the $\Lambda$-action along all
maps. This is possible because
$Rj_*\colon D^+(X_{\mathrm{ét}},\Lambda)\to D^+(Y_{\mathrm{ét}},\Lambda)$
commutes with the forgetful functors to
$D^+(-_{\mathrm{ét}},\mathbf Z/\ell^r\mathbf Z)$ (Stacks, Tag
[0D6J](https://stacks.math.columbia.edu/tag/0D6J)), and because a
$\Lambda$-sheaf is constructible if and only if its underlying sheaf is: on a
finite stratification trivializing the underlying sheaf, the finitely many
endomorphisms giving the action become constant after a further finite
refinement. Finally, truncation triangles extend both conclusions from sheaves
to bounded constructible complexes.
