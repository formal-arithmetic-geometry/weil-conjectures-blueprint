+++
kind = "proof"
of = "sk-lem-tf-sp-defect-exchanges"
uses = ["sk-lem-tf-sp-dnc-functorial", "sk-lem-tf-sp-constant-family"]
+++
Apply the preceding deformation lemma [sk-lem-tf-sp-dnc-functorial], nearby-cycle proper or smooth
exchange, and proper or smooth base change to restriction to the zero section. The resulting
squares for $\epsilon$ commute because the pullback exchange commutes with composition; take their
cofibres. For $f=i$ the source pair is $(Z,Z)$ and $\mathcal D_ZZ=Z\times S$. Its comparison is the
identity after [sk-lem-tf-sp-constant-family], so $C_{Z,Z}=0$. Proper exchange therefore gives
$C_{X,Z}(i_*M)=0$. Apply the exact functor $C_{X,Z}$ to $j_!j^*L\to L\to i_*i^*L$ for the last
assertion.
