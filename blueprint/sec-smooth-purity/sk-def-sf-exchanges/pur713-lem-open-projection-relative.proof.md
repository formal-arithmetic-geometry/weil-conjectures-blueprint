+++
kind = "proof"
of = "pur713-lem-open-projection-relative"
uses = ["pur713-def-relative-tensor", "pur713-input-change-scalars-iso", "pur713-input-coefficient-open", "pur713-input-open-projection"]
+++
Since $\alpha_{j,T}$ is an isomorphism (Input [pur713-input-coefficient-open]), $j^*_TN$ is $j^{-1}_{\mathbf Z}N$ with action transported along $\alpha_{j,T}^{-1}$ (Input [pur713-input-change-scalars-iso]). Both relative tensor products are coequalizers of tensor products over $\mathbf Z$ (Definition [pur713-def-relative-tensor]). The functor $j_{!,\mathbf Z}$ preserves coequalizers, being a left adjoint (Input “Fixed-coefficient open-extension adjunction” (`pur713-input-open-fixed`)), and the abelian projection isomorphisms $\pi_{j,N,M}$ and $\pi_{j,N,\mathcal R_{U,T}\otimes M}$ of Input [pur713-input-open-projection] identify the two parallel pairs, compatibly with the actions by the associativity compatibility in that input. The induced map of coequalizers is $\pi^T_{j,N,M}$, because both are adjoint to the same map; it is therefore an isomorphism.
