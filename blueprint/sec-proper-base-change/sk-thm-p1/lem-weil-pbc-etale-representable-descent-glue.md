+++
id = "lem-weil-pbc-etale-representable-descent-glue"
kind = "lemma"
title = "Gluing the represented sheaf after effective descent"
uses = ["def-pc-scheme", "def-pd-descent-datum", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.etaleRepresentable_descentGlue"]
+++
Let $T$ be a scheme [def-pc-scheme], $E$ a sheaf of sets `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)) on $T_{et}$ [def-weil-pbc-etale-site], and $g:U\to T$ an etale surjection. Let $V\to U$ be etale with a descent datum $D$ [def-pd-descent-datum]. Suppose $e:E|_U\simeq h_V$ on the localized site carries each section over an etale $W\to T$ with two lifts $a,b:W\to U$ to points related by the transport of $D$. Let $P\to T$ be etale and $q:V\to P$ exhibit $V$ as $P\times_T U$. Suppose transport preserves the composite with $q$. Then $E\simeq h_P$ as presheaves on $T_{et}$. No finiteness assumption on $V$ or $P$ is needed.
