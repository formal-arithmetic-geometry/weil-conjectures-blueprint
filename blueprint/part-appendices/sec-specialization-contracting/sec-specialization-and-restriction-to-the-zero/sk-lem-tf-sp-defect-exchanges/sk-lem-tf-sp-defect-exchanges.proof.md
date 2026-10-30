+++
kind = "proof"
of = "sk-lem-tf-sp-defect-exchanges"
uses = ["sk-lem-tf-sp-dnc-functorial", "sk-lem-tf-sp-constant-family"]
+++
We apply Lemma [sk-lem-tf-sp-dnc-functorial], the base change maps of nearby
cycles for proper or smooth morphisms, and proper or smooth base change
for the restriction to the zero section. The resulting squares for
$\tau$ commute because the base change map for pullback is compatible
with composition, and we take their cofibres.
For $f=i$, the source pair is $(Z,Z)$ and
$\mathcal D_ZZ=Z\times S$. In this case $\tau_{Z,Z}$ is the
inverse of the isomorphism of Lemma [sk-lem-tf-sp-constant-family], and
hence $C_{Z,Z}=0$.
Therefore the base change isomorphism for proper maps shows that $C_{X,Z}(i_*M)=0$.
For the last assertion, we apply the exact functor $C_{X,Z}$
to $j_!j^*L\to L\to i_*i^*L$.
