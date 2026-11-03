+++
id = "lem-weil-pbc-henselian-of-nil-maximal-ideal"
kind = "lemma"
title = "A local ring with nil maximal ideal is henselian"
uses = ["def-weil-pbc-henselian-terminology"]
lean = ["henselianLocalRing_of_maximalIdeal_le_nilradical", "Ring.KrullDimLE.nilradical_eq_maximalIdeal", "IsLocalRing.idempotent_lifting_iff_monic_simple_root_lifting"]
order = 2032
+++
Let $R$ be a commutative local ring with maximal ideal $\mathfrak m$. If every element of $\mathfrak m$ is nilpotent, then $R$ is a henselian local ring [def-weil-pbc-henselian-terminology]. In particular every local ring of Krull dimension $0$ (a local ring whose only prime ideal is $\mathfrak m$, for example an Artinian local ring) is henselian, since then $\mathfrak m$ is the nilradical of $R$.
