+++
kind  = "proof"
of    = "sk-def-sfb-dc-setting"
uses = ["sk-thm-nagata-compactification"]
+++
The scheme $\operatorname{Spec}k$ is affine, hence quasi-compact and quasi-separated. So
[lem-sfb-compactification-over-base] with $S=\operatorname{Spec}k$ shows that every morphism
of the setting has a compactification, and $c_f$ is the choice of
[def-sfb-compactification-over-field]. For a compactification $c=(i,p)$ of $f\colon X\to Y$, the
structure morphism $Z\to\operatorname{Spec}k$ is the composite of the proper morphism $p$ with
$Y\to\operatorname{Spec}k$. Both factors are separated and of finite type, hence so is the
composite. The morphisms $p$ and $i$ are over $k$ because $p$ is, by construction, and
$p\circ i=f$ is.
