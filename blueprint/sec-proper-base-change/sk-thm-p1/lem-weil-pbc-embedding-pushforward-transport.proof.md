+++
kind = "proof"
of = "lem-weil-pbc-embedding-pushforward-transport"
+++
For any homeomorphism between arbitrary universes, its equivalence on opens is a dense subsite. Prove preservation and reflection of covering sieves pointwise: forward, factor an arrow of the image sieve and pull membership back by the inverse homeomorphism; reverse, send a covering arrow to its image. Equivalence supplies cover density and local full faithfulness.

Set h:D≃ₜZ to e restricted to D, followed by the inverse of the embedding's homeomorphism to its range. Use sheafCongr on the equivalences of opens from e.symm and h.symm, with the dense-subsite proof, to obtain T and S.

At the top open the inverse open-set functor preserves top, giving the global-sections isomorphism by mapIso of eqToIso. Its naturality is the underlying sheaf morphism's naturality. The two direct-image composites are definitionally equal: h.symm(z) has underlying point e.symm(i(z)). Use Iso.refl under ObjectProperty.isoMk and NatIso.ofComponents.
