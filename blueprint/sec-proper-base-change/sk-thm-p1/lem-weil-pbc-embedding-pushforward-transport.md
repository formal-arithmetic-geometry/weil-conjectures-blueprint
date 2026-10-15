+++
id = "lem-weil-pbc-embedding-pushforward-transport"
kind = "lemma"
title = "Equivalences of sheaf categories identifying the embedded-image direct images"
lean = ["TopCat.embedding_pushforward_transport"]
+++
Let X,Z be topological spaces in universe u, i:Z→X a continuous embedding, Y a topological space in universe u+1, and e:Y≃ₜX a homeomorphism. Let D=e⁻¹(range i), and let j:D→Y be the inclusion. There exist equivalences T:Sh(X,Type(u+1))≌Sh(Y,Type(u+1)) and S:Sh(Z,Type(u+1))≌Sh(D,Type(u+1)), a natural isomorphism Γ(X,−)≅T⋙Γ(Y,−), and a natural isomorphism i_*⋙T≅S⋙j_*. These are direct-image statements, with no inverse-image or adjunction unit assumed.
