---
layout: default
title: "asimov and other workflow tools"
---

<!-- Hero Section -->
<section class="hero">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-8 mx-auto text-center">
        <h1>asimov and other workflow tools</h1>
        <p class="lead">Where asimov sits relative to other research workflow software, and when each tool is the better fit.</p>
      </div>
    </div>
  </div>
</section>

<!-- Intro -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">What level asimov works at</h2>
        <p>asimov orchestrates <strong>analyses</strong> &mdash; long-running, heavyweight, individually reviewed units of scientific work, such as a Bayesian parameter-estimation run &mdash; across the <strong>subjects</strong> of a catalogue, such as the gravitational-wave events in GWTC-3. It does not build or manage the fine-grained task graph inside an analysis: that is delegated to whatever pipeline is being run (for example, <code>bilby_pipe</code> writes its own HTCondor DAG). asimov's job is the layer above that: which analyses exist for which subjects, what each depends on, what its configuration was, whether it has been reviewed, and where it currently stands.</p>
        <p>This is a different granularity from most workflow engines, which schedule individual tasks or files within a single pipeline run. The comparison below is offered in that spirit &mdash; these tools solve related but not identical problems, and several are commonly used <em>together</em> with asimov rather than instead of it.</p>
      </div>
    </div>
  </div>
</section>

<!-- Comparison Table -->
<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">Feature comparison</h2>
        <p class="section-subtitle">A comparison against other established workflow and provenance tools. Where a detail is uncertain, it is described generally rather than guessed.</p>

        <div class="table-responsive mt-5">
          <table class="table table-bordered align-middle">
            <thead class="table-light">
              <tr>
                <th style="width: 18%;">&nbsp;</th>
                <th style="width: 16.4%;">asimov</th>
                <th style="width: 16.4%;">AiiDA</th>
                <th style="width: 16.4%;">Snakemake</th>
                <th style="width: 16.4%;">Nextflow</th>
                <th style="width: 16.4%;">Apache Airflow</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Unit of work</strong></td>
                <td>An analysis of a subject (e.g. one event's parameter estimation)</td>
                <td>A calculation or workflow step in a provenance graph</td>
                <td>A rule producing output files from input files</td>
                <td>A process operating on items in a dataflow</td>
                <td>A task within a DAG, typically scheduled on a recurring basis</td>
              </tr>
              <tr>
                <td><strong>Workflow specification</strong></td>
                <td>Declarative YAML blueprints (project/subject/analysis) with hierarchical, inherited settings; dependencies expressed with <code>needs:</code></td>
                <td>Python API (AiiDA work chains/work functions); calculations and their inputs/outputs recorded as a graph</td>
                <td>A Snakefile: a Python-embedded DSL of file-pattern rules</td>
                <td>A dataflow DSL, built on Groovy, describing channels and processes</td>
                <td>Python DAGs of operators, defined as code</td>
              </tr>
              <tr>
                <td><strong>Provenance &amp; record-keeping</strong></td>
                <td>A ledger (YAML or database) recording each analysis's configuration and state; generated configs are committed to git</td>
                <td>A full provenance graph stored in a database, capturing every calculation's inputs, outputs, and code version</td>
                <td>Rule graph and run metadata; provenance is largely implicit in the file dependency graph</td>
                <td>Execution trace and reports (e.g. via Nextflow Tower/Seqera Platform); provenance follows the dataflow graph</td>
                <td>DAG run history and task logs in its metadata database; not a scientific provenance graph</td>
              </tr>
              <tr>
                <td><strong>Execution backends</strong></td>
                <td>HTCondor and Slurm</td>
                <td>Local execution plus remote HPC schedulers (Slurm, PBS, SGE, LSF, and others) through scheduler plugins, over local or SSH transports</td>
                <td>Local execution, most HPC schedulers, and several cloud/cluster executors</td>
                <td>Local execution, most HPC schedulers, and cloud executors including Kubernetes</td>
                <td>Local or distributed execution via its scheduler and executors (e.g. Celery, Kubernetes); not HPC-scheduler-oriented</td>
              </tr>
              <tr>
                <td><strong>Human review / sign-off</strong></td>
                <td>Built in: a review module records sign-off decisions against each analysis in the ledger</td>
                <td>Not a built-in concept; review would be handled outside the tool</td>
                <td>Not a built-in concept</td>
                <td>Not a built-in concept</td>
                <td>Not a built-in concept; task success/failure is tracked, not scientific review</td>
              </tr>
              <tr>
                <td><strong>Primary community</strong></td>
                <td>Gravitational-wave astronomy (LIGO/Virgo/KAGRA); domain-agnostic core</td>
                <td>Computational materials science and atomistic simulation</td>
                <td>Bioinformatics and general computational science</td>
                <td>Bioinformatics (nf-core) and general scientific pipelines</td>
                <td>Data engineering</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- When to use which -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">When to use which</h2>
        <p><strong>asimov</strong> fits when a project runs many heavyweight analyses per subject, across a whole catalogue, using several different analysis codes, and needs a durable, reviewable record of what was run and why &mdash; the situation LVK parameter-estimation catalogues (GWTC-2, 2.1, 3, and 4.0) are in.</p>
        <p><strong>Snakemake</strong> and <strong>Nextflow</strong> are strong choices for file-oriented pipelines where the unit of work is a transformation from input files to output files, and where container-based portability and a large existing library of community workflows (e.g. nf-core) are valuable.</p>
        <p><strong>AiiDA</strong> is the natural choice when full, queryable data provenance of atomistic or materials-science simulations is the goal, with every calculation's inputs, outputs, and code versions captured in a graph database.</p>
        <p><strong>Apache Airflow</strong> suits recurring, schedule-driven data-engineering jobs &mdash; ETL pipelines, periodic reports &mdash; rather than one-off scientific analyses.</p>
        <p>These tools are not mutually exclusive with asimov. A pipeline that asimov orchestrates as a single analysis may itself be implemented as a Snakemake or Nextflow workflow underneath; asimov's ledger and review layer sit above that, tracking the analysis as a whole rather than its internal steps.</p>
      </div>
    </div>
  </div>
</section>

<!-- Current limitations -->
<section class="section bg-light">
  <div class="container">
    <div class="row">
      <div class="col-lg-10 mx-auto">
        <h2 class="section-title">Current limitations</h2>
        <ul>
          <li>Submission is currently limited to HTCondor and Slurm; there is no support for PBS, SGE, LSF, or cloud/Kubernetes execution.</li>
          <li>asimov does not manage containers itself &mdash; any containerization is left to the pipeline being run.</li>
          <li>The plugin ecosystem is presently concentrated on gravitational-wave analysis codes (Bilby, LALInference, RIFT, BayesWave, PESummary, and similar).</li>
          <li>There is no graphical monitoring UI at this time; status is inspected through the command line and generated HTML reports.</li>
          <li><a href="https://github.com/etive-io/asimov-exoplanet">asimov-exoplanet</a> is an early example of the ledger/blueprint/plugin model applied outside gravitational-wave astronomy, showing the approach is not inherently domain-specific, though using it in a new domain currently means writing new pipeline plugins.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- Closing -->
<section class="section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mx-auto text-center">
        <h2 class="section-title">Learn more</h2>
        <p class="lead text-muted mb-4">See asimov in action, or browse the available pipeline plugins.</p>
        <div>
          <a href="{{ '/tutorials/09-gw150914-quickstart/' | relative_url }}" class="btn btn-primary btn-lg me-2">GW150914 quickstart</a>
          <a href="{{ '/plugins/' | relative_url }}" class="btn btn-outline-primary btn-lg">Plugin registry</a>
        </div>
      </div>
    </div>
  </div>
</section>
