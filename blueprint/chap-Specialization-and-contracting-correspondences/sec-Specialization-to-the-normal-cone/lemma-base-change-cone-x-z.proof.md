+++
kind = "proof"
of = "lemma-base-change-cone-x-z"
order = 1625
uses = ["definition-pro-etale-base-change-map", "theorem-proper-base-change-classical-pro", "lemma-nearby-cycles-constant-family", "lemma-functoriality-deformation"]
+++
Both the source and the target of $\tau$ are compatible with proper
direct image and smooth pullback, so the cone is as well. To prove the
vanishing on $i_*M$, we reduce to the pair $(Z,Z)$, where the
deformation is a constant family.

By Lemma [lemma-functoriality-deformation], $f$ induces a morphism
$\widetilde f$ of deformations, which is proper if $f$ is proper and
smooth if $f$ is smooth. To it we apply the base change maps of
nearby cycles, together with proper or smooth base change for the
restriction to the zero section.  The resulting squares for
$\tau$ commute because the base change map for pullback is compatible
with composition, and their cofibres give the two isomorphisms.
For $f=i$, the source pair is $(Z,Z)$ and
$\mathcal D_ZZ=Z\times S$, so $\tau_{Z,Z}$ is the
inverse of the isomorphism of Lemma [lemma-nearby-cycles-constant-family].
Hence $C_{Z,Z}=0$. As $i$ is proper, the first isomorphism gives
$C_{X,Z}(i_*M)=0$.
The last assertion follows by applying the exact functor $C_{X,Z}$
to $j_!j^*L\to L\to i_*i^*L$.
