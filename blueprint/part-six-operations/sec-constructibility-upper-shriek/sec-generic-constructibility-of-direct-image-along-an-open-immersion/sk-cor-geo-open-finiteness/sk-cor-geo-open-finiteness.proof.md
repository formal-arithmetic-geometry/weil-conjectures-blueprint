+++
kind = "proof"
of = "sk-cor-geo-open-finiteness"
uses = ["sk-thm-geo-generic-open"]
+++
We argue on the étale site.

For a constructible $\Fell$-sheaf this is
Theorem [sk-thm-geo-generic-open] with $S=\operatorname{Spec}k$. A
constructible sheaf killed by $\ell^r$ has a finite filtration by the
images of multiplication by powers of $\ell$, with constructible
$\Fell$-sheaves as successive quotients. The long exact cohomology
sequences then yield (7.22), and morphisms between the resulting triangles give
the base change assertion. For a finite $\ell$-primary ring
$\Lambda$, we apply this to the underlying
$\mathbf Z/\ell^r\mathbf Z$-sheaf and carry the $\Lambda$-action
along all maps. We may do so for two reasons. First,
$Rj_*:D^+(X_{\acute{e}t},\Lambda)\to D^+(Y_{\acute{e}t},\Lambda)$ commutes
with the forgetful functors to
$D^+(-_{\acute{e}t},\mathbf Z/\ell^r\mathbf Z)$ [Stacks, Tag 0D6J](https://stacks.math.columbia.edu/tag/0D6J). Second, a
$\Lambda$-sheaf is constructible if and only if its underlying sheaf
is. Indeed, on a stratum where the underlying sheaf is finite locally
constant, the action of each of the finitely many elements of $\Lambda$
is a section of the finite locally constant sheaf of endomorphisms, and
hence it is constant étale locally. So the $\Lambda$-module is
locally constant on that stratum. Finally, truncation triangles extend both conclusions from
sheaves to bounded constructible complexes.
