+++
id = "lem-weil-pbc-filtered-colimit-normal-ring-domain"
kind = "lemma"
title = "Localizations of a filtered colimit of rings with domain localizations are domains"
lean = ["CommRingCat.filtered_colimit_localization_isDomain"]
order = 1868
+++
Let $I$ be a small filtered category and $i\mapsto R_i$ a functor from $I$ to commutative rings with colimit $R=\varinjlim_IR_i$. Assume that for every $i\in I$ and every prime ideal $\mathfrak q\subset R_i$ the localization $(R_i)_{\mathfrak q}$ is a domain. Then for every prime ideal $\mathfrak p\subset R$ the localization $R_{\mathfrak p}$ is a domain.
