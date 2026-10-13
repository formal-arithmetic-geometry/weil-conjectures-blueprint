+++
id = "pur9-input-constructible-flat-model"
kind = "remark"
title = "Constructible flat models on the étale site"
order = 2177
tags = ["latex:bpinput"]
uses = ["pur713-def-finite-constructible", "pur7710-input-constructible-serre", "pur9-def-flat-sheaf", "pur9-def-tor-amplitude-etale", "pur9-lem-flat-model"]
+++
Let $T$ be a $k$-scheme of finite type and $K\in D^b_c(T_{\Et},\mathcal O_E/\varpi^n)$ with Tor amplitude in $[u,v]$ (Definition [pur9-def-tor-amplitude-etale]). Then $K$ is isomorphic to a complex $P$ of flat constructible sheaves of $\mathcal O_E/\varpi^n$-modules on $T_{\Et}$ (Definitions [pur9-def-flat-sheaf] and [pur713-def-finite-constructible]) with $P^q=0$ for $q\notin[u,v]$. *Status:* imported. The source argument resolves $K$ in decreasing degree by finite sums of $j_{V!}(\mathcal O_E/\varpi^n)_V$, $j_V:V\to T$ étale with $V$ affine, using that every constructible sheaf is a quotient of such a sum (Stacks Project, Tag `095M`; SGA $4\tfrac12$, Rapport, 4.6–4.8) and Input [pur7710-input-constructible-serre], and then truncates as in Lemma [pur9-lem-flat-model].
