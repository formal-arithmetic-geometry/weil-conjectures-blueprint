+++
kind = "proof"
of = "corollary-open-direct-image-over-field"
order = 580
+++
We argue on the étale site. The theorem gives the case of
$\Fell$-sheaves, and we pass to $\mathbf Z/\ell^r$-sheaves by
filtrations, to $\Lambda$-sheaves by forgetting the $\Lambda$-structure,
and to complexes by truncation.

For a constructible $\Fell$-sheaf this is
Theorem [theorem-generic-constructibility-base-change-rj] with $S=\operatorname{Spec}k$. A
constructible sheaf $F$ killed by $\ell^r$ has the finite filtration
$F\supset\ell F\supset\cdots\supset\ell^rF=0$. Its successive quotients
$\ell^iF/\ell^{i+1}F$ are constructible and killed by $\ell$, that is,
constructible $\Fell$-sheaves. Each short exact sequence in the filtration
is a triangle in the derived category, and $Rj_*$ carries it to a
triangle. By induction on $r$, the long exact cohomology sequences of
these triangles give (6.22). The base change maps form
morphisms between the resulting triangles, and they are isomorphisms by
the five lemma.

For a finite $\ell$-primary ring $\Lambda$, we apply this to the
underlying $\mathbf Z/\ell^r\mathbf Z$-sheaf and carry the
$\Lambda$-action along all maps. This is possible for two reasons. First,
$Rj_*:D^+(X_{\acute{e}t},\Lambda)\to D^+(Y_{\acute{e}t},\Lambda)$ commutes with the
forgetful functors to $D^+(-_{\acute{e}t},\mathbf Z/\ell^r\mathbf Z)$
[Stacks, [0D6J](https://stacks.math.columbia.edu/tag/0D6J)]. Second, a $\Lambda$-sheaf is constructible if and only if
its underlying sheaf is. To see this, consider a stratum where the
underlying sheaf is finite locally constant. There the action of each of
the finitely many elements of $\Lambda$ is a section of the finite locally
constant sheaf of endomorphisms, hence constant étale locally. Therefore
the $\Lambda$-module is locally constant on that stratum. Truncation triangles extend both
conclusions from sheaves to bounded constructible complexes.
