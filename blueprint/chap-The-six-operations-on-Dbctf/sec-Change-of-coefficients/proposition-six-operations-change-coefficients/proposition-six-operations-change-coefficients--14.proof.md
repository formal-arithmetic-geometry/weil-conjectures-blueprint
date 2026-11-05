+++
kind = "proof"
of = "proposition-six-operations-change-coefficients--14"
order = 645029
uses = ["proposition-topos-functoriality"]
+++
For the conjugate comparison under the flatness hypothesis, first prove that restriction of scalars commutes with the direct-image composition isomorphisms on complexes. Derive this identity using K-injective representatives, then conjugate it along the derived adjunctions. This is `derivedPullIso_hom_app_comp`, packaged as `derivedPullIsoCompCoherence`.

For an arbitrary coefficient change, prove the composition identity for the underived pullback comparisons. The derived comparisons agree with these maps through the counits on K-flat representatives (`derivedUpperStarExtendScalarsIsoFac`). The composition identity therefore descends to the derived category.
