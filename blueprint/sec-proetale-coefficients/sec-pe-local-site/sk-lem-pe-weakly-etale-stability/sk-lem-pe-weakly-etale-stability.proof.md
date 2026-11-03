+++
kind = "proof"
of = "sk-lem-pe-weakly-etale-stability"
+++
Base change preserves flatness of a morphism and its diagonal. For a
composite $V\to U\to X$, the diagonal $\Delta_{V/X}$ is $\Delta_{V/U}$
followed by $V\times_UV\to V\times_XV$, which is a base change of
$\Delta_{U/X}$, and both of these are flat.
For an $X$-morphism $h:U\to V$, the graph
$U\to U\times_XV$ is a base change of the flat diagonal of $V/X$, and
the projection $U\times_XV\to V$ is flat because $U/X$ is flat.
Their composite $h$ is therefore flat, and $\Delta_h$ is flat as a
base change of $\Delta_{U/X}$. Zariski locality follows from the fact that
flatness is Zariski local.
For ind-étale ring maps, base change is clear because tensor products
commute with filtered colimits. For composition, an étale algebra over
a filtered colimit $\varinjlim_\alpha B_\alpha$ is of finite
presentation, hence is the base change of an étale algebra over some
$B_\alpha$, which is étale over $R$.
