+++
kind = "proof"
of = "theorem-bounded-below-cohomology-comparison--1"
order = 123002
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "proposition-topos-functoriality--1", "proposition-topos-functoriality--2", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "proposition-w-local-components--1", "example-locally-constant-functions-w-local--1", "proposition-pro-etale-affines-form-basis--2", "theorem-classical-sheaves-essential-image--1", "lemma-acyclicity-pulled-back-injectives--1"]
+++
The category $\Sh(X_{\acute{e}t},\mathcal A)$ is Grothendieck abelian, so we may
choose a bounded-below injective resolution $K\to I^\bullet$. Since
$\nu_X^*$ is exact, $\nu_X^*I^\bullet$ represents $\nu_X^*K$.

Each $\nu_X^*I^q$ is $\nu_{X,*}$-acyclic. For sheaves of
$\Lambda$-modules this is Lemma [lemma-acyclicity-pulled-back-injectives].
Its proof applies verbatim to an injective sheaf $I$ with values in
$\mathcal A$, once the free sheaves of $\Lambda$-modules on the nerve of a
covering are replaced as follows. For an object $a$ of $\mathcal A$ and an
étale object $U$, let $a_U$ be the sheaf associated with
$V\mapsto\bigoplus_{\Hom(V,U)}a$, so that
$\Hom(a_U,I)=\Hom_{\mathcal A}(a,I(U))$. For an étale covering of $V$,
the augmented complex of the sheaves $a_U$ on its nerve is exact: locally
the covering has a section, and then the complex is $a$ tensored with the
chain complex of the Čech nerve of a nonempty set, which is
contractible. As $I$ is injective, applying $\Hom(-,I)$ shows that
$\Hom_{\mathcal A}(a,-)$ of the augmented Čech complex of $I$ is exact
for every $a$. Taking for $a$ the cycles in a given degree shows that the
Čech complex of $I$ itself has no positive cohomology, and the rest of
the argument is unchanged.

By Theorem [theorem-classical-sheaves-essential-image], $\nu_X^*$ is
fully faithful on $\mathcal A$-valued sheaves, so the unit
$I^q\to\nu_{X,*}\nu_X^*I^q$ is an isomorphism for every $q$. Hence
$R\nu_{X,*}\nu_X^*K$ is computed by the complex
$\nu_{X,*}\nu_X^*I^\bullet\simeq I^\bullet$, and the derived unit is
identified with the resolution $K\to I^\bullet$. This proves
(2.7). For $\mathcal A=\operatorname{Mod}(\Lambda)$ the derived
categories involved are $D^+(X_{\acute{e}t},\Lambda)$ and
$D^+(X_{\mathrm{pro}\acute{e}t},\Lambda)$.

*Source:* the proof of Theorem [theorem-bounded-below-cohomology-comparison].
