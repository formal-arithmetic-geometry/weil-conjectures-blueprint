+++
id = "lem-weil-pbc-ring-sheafification-underlying-sets"
kind = "lemma"
title = "Sheafification of a presheaf of rings has as underlying sheaf of sets the sheafification of sets"
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-sheafification", "def-weil-pbc-constant-sheaf"]
refines = "proof/lem-weil-pbc-sheaves-killed-by-n-zmod-modules"
lean = ["CategoryTheory.sheafifyComposeIso"]
tags = ["sheaf-dag", "mathlib"]
+++
Let $T$ be a scheme, $T_{\Et}$ its small etale site [def-weil-pbc-etale-site], $P$ a presheaf of commutative rings (or of rings) on $T_{\Et}$, and $\eta:P\to P^\#$ its sheafification in sheaves of (commutative) rings [def-weil-pbc-sheafification]. Write $|-|$ for the underlying presheaf of sets. Then $|P^\#|$ is a sheaf of sets and $|\eta|:|P|\to|P^\#|$ is a sheafification of the presheaf of sets $|P|$: every morphism of presheaves of sets from $|P|$ to a sheaf of sets $H$ factors uniquely through $|\eta|$. In particular, for a ring $R$, the constant sheaf of rings $\underline R$ [def-weil-pbc-constant-sheaf] has as underlying sheaf of sets, with the canonical map from the constant presheaf $U\mapsto R$, the constant sheaf of sets on the underlying set of $R$.
