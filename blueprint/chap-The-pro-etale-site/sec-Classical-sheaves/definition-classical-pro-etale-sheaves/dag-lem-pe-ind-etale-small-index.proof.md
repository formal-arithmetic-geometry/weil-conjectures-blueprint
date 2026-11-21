+++
kind = "proof"
of = "dag-lem-pe-ind-etale-small-index"
tags = ["sheaf-dag"]
+++
1. For R → B, let E be the category of finitely presented étale R-algebras mapping to B. Finite presentations and small hom sets make E essentially universe-u small. It is filtered: R is initial, tensor products give coproducts, and coequalizers are étale quotients. Indeed equalizers of two maps of affine étale R-schemes are pullbacks of an affine étale diagonal, which is open and closed; they are affine étale. The small colimit C of E is ind-étale with a map p:C→B.
2. The given larger diagram maps compatibly into E and hence into C. Its colimit property gives s:B→C with p s=id, checked on every stage. Nonemptiness ensures s is an R-algebra map. Thus B is a retract of C. For e=s p, the sequential diagram C --e--> C --e--> ... has colimit B: cocone maps satisfy a_n=a_(n+1)e, and idempotence forces a_n e=a_n and all components equal; their unique factorization through p is a_0 s. Flatten the countable diagram of small étale presentations using finite presentability of étale algebras (ObjectProperty.ind_ind). Hence B has a small filtered étale presentation.
