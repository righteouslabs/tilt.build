### AUTO-GENERATED ###
# This file was auto-generated by 'tilt dump api-docs' as part of a Tilt release.
# To make changes, modify the following file in the Tilt repository:
#   internal/tiltfile/api/v1alpha1/__init__.py
# Generated by Tilt version v0.33.8, built 2023-11-30
### AUTO-GENERATED ###

from typing import Dict, List, Optional

# AUTOGENERATED by github.com/tilt-dev/tilt-starlark-docs-codegen
# DO NOT EDIT MANUALLY


class ConfigMapDisableSource:
  """Specifies a ConfigMap to control a DisableSource
"""
  pass



class DisableSource:
  """Points at a thing that can control whether something is disabled
"""
  pass



class ExecAction:
  """ExecAction describes a "run in container" action.
"""
  pass



class Forward:
  """Forward defines a port forward to execute on a given pod.
"""
  pass



class HTTPGetAction:
  """HTTPGetAction describes an action based on HTTP Get requests.
"""
  pass



class HTTPHeader:
  """HTTPHeader describes a custom header to be used in HTTP probes
"""
  pass



class Handler:
  """Handler defines a specific action that should be taken in a probe.
"""
  pass



class IgnoreDef:
  """Describes sets of file paths that the FileWatch should ignore.
"""
  pass



class KubernetesApplyCmd:
  """
"""
  pass



class KubernetesDiscoveryTemplateSpec:
  """
"""
  pass



class KubernetesImageLocator:
  """Finds image references in Kubernetes YAML.
"""
  pass



class KubernetesImageObjectDescriptor:
  """
"""
  pass



class KubernetesWatchRef:
  """KubernetesWatchRef is similar to v1.ObjectReference from the Kubernetes API and is used to determine
  what objects should be reported on based on discovery.
"""
  pass



class LabelSelector:
  """
"""
  pass



class LabelSelectorRequirement:
  """
"""
  pass



class ObjectSelector:
  """Selector for any Kubernetes-style API.
"""
  pass



class PodLogStreamTemplateSpec:
  """PodLogStreamTemplateSpec describes common attributes for PodLogStreams
  that can be shared across pods.
"""
  pass



class PortForwardTemplateSpec:
  """PortForwardTemplateSpec describes common attributes for PortForwards
  that can be shared across pods.
"""
  pass



class Probe:
  """Probe describes a health check to be performed to determine whether it is
  alive or ready to receive traffic.
"""
  pass



class RestartOnSpec:
  """RestartOnSpec indicates the set of objects that can trigger a restart of this object.
"""
  pass



class StartOnSpec:
  """StartOnSpec indicates the set of objects that can trigger a start/restart of this object.
"""
  pass



class TCPSocketAction:
  """TCPSocketAction describes an action based on opening a socket
"""
  pass



class UIBoolInputSpec:
  """Describes a boolean checkbox input field attached to a button.
"""
  pass



class UIComponentLocation:
  """UIComponentLocation specifies where to put a UI component.
"""
  pass



class UIHiddenInputSpec:
  """Describes a hidden input field attached to a button,
  with a value to pass on any submit.
"""
  pass



class UIInputSpec:
  """Defines an Input to render in the UI.
  If UIButton is analogous to an HTML <form>,
  UIInput is analogous to an HTML <input>.
"""
  pass



class UITextInputSpec:
  """Describes a text input field attached to a button.
"""
  pass


def cmd(
  name: str,
  labels: Dict[str, str] = None,
  annotations: Dict[str, str] = None,
  args: List[str] = None,
  dir: str = "",
  env: List[str] = None,
  readiness_probe: Optional[Probe] = None,
  restart_on: Optional[RestartOnSpec] = None,
  start_on: Optional[StartOnSpec] = None,
  disable_source: Optional[DisableSource] = None,
):
  """
  Cmd represents a process on the host machine.
  
  When the process exits, we will make a best-effort attempt
  (within OS limitations) to kill any spawned descendant processes.
  

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    args: Command-line arguments. Must have length at least 1.
    dir: Process working directory.
      
      If the working directory is not specified, the command is run
      in the default Tilt working directory.
      
    env: Additional variables process environment.
      
      Expressed as a C-style array of strings of the form ["KEY1=VALUE1", "KEY2=VALUE2", ...].
      
      Environment variables are layered on top of the environment variables
      that Tilt runs with.
      
    readiness_probe: Periodic probe of service readiness.
      
    restart_on: Indicates objects that can trigger a restart of this command.
      
      When a restart is triggered, Tilt will try to gracefully shutdown any
      currently running process, waiting for it to exit before starting a new
      process. If the process doesn't shutdown within the allotted time, Tilt
      will kill the process abruptly.
      
      Restarts can happen even if the command is already done.
      
      Logs of the current process after the restart are discarded.
    start_on: Indicates objects that can trigger a start/restart of this command.
      
      Restarts behave the same as RestartOn. The key difference is that
      a Cmd with any StartOn triggers will not have its command run until its
      StartOn is satisfied.
    disable_source: Specifies how to disable this.
      
"""
  pass
def config_map(
  name: str,
  labels: Dict[str, str] = None,
  annotations: Dict[str, str] = None,
  data: Dict[str, str] = None,
):
  """
  ConfigMap stores unstructured data that other controllers can read and write.
  
  Useful for sharing data from one system and subscribing to it from another.
  

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    data: Data contains the configuration data.
      Each key must consist of alphanumeric characters, '-', '_' or '.'.
"""
  pass
def extension(
  name: str,
  labels: Dict[str, str] = None,
  annotations: Dict[str, str] = None,
  repo_name: str = "",
  repo_path: str = "",
  args: List[str] = None,
):
  """
  Extension defines an extension that's evaluated on Tilt startup.

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    repo_name: RepoName specifies the ExtensionRepo object where we should find this extension.
      
      The Extension controller should watch for changes to this repo, and
      may update if this repo is deleted or moved.
    repo_path: RepoPath specifies the path to the extension directory inside the repo.
      
      Once the repo is downloaded, this path should point to a directory with a
      Tiltfile as the main "entrypoint" of the extension.
    args: Arguments to the Tiltfile loaded by this extension.
      
      Arguments can be positional (['a', 'b', 'c']) or flag-based ('--to-edit=a').
      By default, a list of arguments indicates the list of services in the tiltfile
      that should be enabled.
      
"""
  pass
def extension_repo(
  name: str,
  labels: Dict[str, str] = None,
  annotations: Dict[str, str] = None,
  url: str = "",
  ref: str = "",
):
  """
  ExtensionRepo specifies a repo or folder where a set of extensions live.

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    url: The URL of the repo.
      
      Allowed:
      https: URLs that point to a public git repo
      file: URLs that point to a location on disk.
    ref: A reference to sync the repo to. If empty, Tilt will always update
      the repo to the latest version.
"""
  pass
def file_watch(
  name: str,
  labels: Dict[str, str] = None,
  annotations: Dict[str, str] = None,
  watched_paths: List[str] = None,
  ignores: List[IgnoreDef] = None,
  disable_source: Optional[DisableSource] = None,
):
  """
  FileWatch

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    watched_paths: WatchedPaths are paths of directories or files to watch for changes to. It cannot be empty.
      
    ignores: Ignores are optional rules to filter out a subset of changes matched by WatchedPaths.
    disable_source: Specifies how to disable this.
      
"""
  pass
def kubernetes_apply(
  name: str,
  labels: Dict[str, str] = None,
  annotations: Dict[str, str] = None,
  yaml: str = "",
  image_maps: List[str] = None,
  image_locators: List[KubernetesImageLocator] = None,
  timeout: str = "",
  kubernetes_discovery_template_spec: Optional[KubernetesDiscoveryTemplateSpec] = None,
  port_forward_template_spec: Optional[PortForwardTemplateSpec] = None,
  pod_log_stream_template_spec: Optional[PodLogStreamTemplateSpec] = None,
  discovery_strategy: str = "",
  disable_source: Optional[DisableSource] = None,
  cmd: Optional[KubernetesApplyCmd] = None,
  restart_on: Optional[RestartOnSpec] = None,
):
  """
  KubernetesApply specifies a blob of YAML to apply, and a set of ImageMaps
  that the YAML depends on.
  
  The KubernetesApply controller will resolve the ImageMaps into immutable image
  references. The controller will process the spec YAML, then apply it to the cluster.
  Those processing steps might include:
  
  - Injecting the resolved image references.
  - Adding custom labels so that Tilt can track the progress of the apply.
  - Modifying image pull rules to ensure the image is pulled correctly.
  
  The controller won't apply anything until all ImageMaps resolve to real images.
  
  The controller will watch all the image maps, and redeploy the entire YAML if
  any of the maps resolve to a new image.
  
  The status field will contain both the raw applied object, and derived fields
  to help other controllers figure out how to watch the apply progress.
  

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    yaml: YAML to apply to the cluster.
      
      Exactly one of YAML OR Cmd MUST be provided.
      
    image_maps: Names of image maps that this applier depends on.
      
      The controller will watch all the image maps, and redeploy the entire YAML
      if any of the maps resolve to a new image.
      
    image_locators: Descriptors of how to find images in the YAML.
      
      Needed when injecting images into CRDs.
      
    timeout: The timeout on the apply operation.
      
      We've had problems with both:
      1) CRD apiservers that take an arbitrarily long time to apply, and
      2) Infinite loops in the apimachinery
      So we offer the ability to set a timeout on Kubernetes apply operations.
      
      The default timeout is 30s.
      
    kubernetes_discovery_template_spec: KubernetesDiscoveryTemplateSpec describes how we discover pods
      for resources created by this Apply.
      
      If not specified, the KubernetesDiscovery controller will listen to all pods,
      and follow owner references to find the pods owned by these resources.
      
    port_forward_template_spec: PortForwardTemplateSpec describes the data model for port forwards
      that KubernetesApply should set up.
      
      Underneath the hood, we'll create a KubernetesDiscovery object that finds
      the pods and sets up the port-forwarding. Only one PortForward will be
      active at a time.
      
    pod_log_stream_template_spec: PodLogStreamTemplateSpec describes the data model for PodLogStreams
      that KubernetesApply should set up.
      
      Underneath the hood, we'll create a KubernetesDiscovery object that finds
      the pods and sets up the pod log streams.
      
      If no template is specified, the controller will stream all
      pod logs available from the apiserver.
      
    discovery_strategy: DiscoveryStrategy describes how we set up pod watches for the applied
      resources. This affects all systems that attach to pods, including
      PortForwards, PodLogStreams, resource readiness, and live-updates.
      
    disable_source: Specifies how to disable this.
      
    cmd: Cmd is a custom command to generate the YAML to apply.
      
      The Cmd MUST return valid Kubernetes YAML for the entities it applied to the cluster.
      
      Exactly one of YAML OR Cmd MUST be provided.
      
    restart_on: RestartOn determines external triggers that will result in an apply.
      
"""
  pass
def kubernetes_discovery(
  name: str,
  labels: Dict[str, str] = None,
  annotations: Dict[str, str] = None,
  watches: List[KubernetesWatchRef] = None,
  extra_selectors: List[LabelSelector] = None,
  port_forward_template_spec: Optional[PortForwardTemplateSpec] = None,
  pod_log_stream_template_spec: Optional[PodLogStreamTemplateSpec] = None,
):
  """
  KubernetesDiscovery

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    watches: Watches determine what resources are discovered.
      
      If a discovered resource (e.g. Pod) matches the KubernetesWatchRef UID exactly, it will be reported.
      If a discovered resource is transitively owned by the KubernetesWatchRef UID, it will be reported.
    extra_selectors: ExtraSelectors are label selectors that will force discovery of a Pod even if it does not match
      the AncestorUID.
      
      This should only be necessary in the event that a CRD creates Pods but does not set an owner reference
      to itself.
    port_forward_template_spec: PortForwardTemplateSpec describes the data model for port forwards
      that KubernetesDiscovery should set up.
      
      The KubernetesDiscovery controller will choose a "best" candidate
      for attaching the port-forwarding. Only one PortForward will be
      active at a time.
      
    pod_log_stream_template_spec: PodLogStreamTemplateSpec describes the data model for PodLogStreams
      that KubernetesDiscovery should set up.
      
      The KubernetesDiscovery controller will attach PodLogStream objects
      to all active pods it discovers.
      
      If no template is specified, the controller will stream all
      pod logs available from the apiserver.
      
"""
  pass
def ui_button(
  name: str,
  labels: Dict[str, str] = None,
  annotations: Dict[str, str] = None,
  location: UIComponentLocation = None,
  text: str = "",
  icon_name: str = "",
  icon_svg: str = "",
  disabled: bool = False,
  requires_confirmation: bool = False,
  inputs: List[UIInputSpec] = None,
):
  """
  UIButton

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    location: Location associates the button with another component for layout.
    text: Text to appear on the button itself or as hover text (depending on button location).
    icon_name: IconName is a Material Icon to appear next to button text or on the button itself (depending on button location).
      
      Valid values are icon font ligature names from the Material Icons set.
      See https://fonts.google.com/icons for the full list of available icons.
      
      If both IconSVG and IconName are specified, IconSVG will take precedence.
      
    icon_svg: IconSVG is an SVG to use as the icon to appear next to button text or on the button itself (depending on button
      location).
      
      This should be an <svg> element scaled for a 24x24 viewport.
      
      If both IconSVG and IconName are specified, IconSVG will take precedence.
      
    disabled: If true, the button will be rendered, but with an effect indicating it's
      disabled. It will also be unclickable.
      
    requires_confirmation: If true, the UI will require the user to click the button a second time to
      confirm before taking action
      
    inputs: Any inputs for this button.
"""
  pass

def config_map_disable_source(
  name: str = "",
  key: str = "",
) -> ConfigMapDisableSource:
  """
  Specifies a ConfigMap to control a DisableSource

  Args:
    name: The name of the ConfigMap
    key: The key where the enable/disable state is stored.
"""
  pass

def disable_source(
  config_map: Optional[ConfigMapDisableSource] = None,
) -> DisableSource:
  """
  Points at a thing that can control whether something is disabled

  Args:
    config_map: This DisableSource is controlled by a ConfigMap
"""
  pass

def exec_action(
  command: List[str] = None,
) -> ExecAction:
  """
  ExecAction describes a "run in container" action.

  Args:
    command: Command is the command line to execute inside the container, the working directory for the
      command  is root ('/') in the container's filesystem. The command is simply exec'd, it is
      not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use
      a shell, you need to explicitly call out to that shell.
      Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
"""
  pass

def forward(
  local_port: int = 0,
  container_port: int = 0,
  host: str = "",
) -> Forward:
  """
  Forward defines a port forward to execute on a given pod.

  Args:
    local_port: The port to expose on the current machine.
      
      If not specified (or 0), a random free port will be chosen and can
      be discovered via the status once established.
      
    container_port: The port on the Kubernetes pod to connect to. Required.
    host: Optional host to bind to on the current machine (localhost by default)
      
"""
  pass

def http_get_action(
  path: str = "",
  port: int = 0,
  host: str = "",
  scheme: str = "",
  http_headers: List[HTTPHeader] = None,
) -> HTTPGetAction:
  """
  HTTPGetAction describes an action based on HTTP Get requests.

  Args:
    path: Path to access on the HTTP server.
    port: Name or number of the port to access on the container.
      Number must be in the range 1 to 65535.
    host: Host name to connect to, defaults to the pod IP. You probably want to set
      "Host" in httpHeaders instead.
    scheme: Scheme to use for connecting to the host.
      Defaults to HTTP.
    http_headers: Custom headers to set in the request. HTTP allows repeated headers.
"""
  pass

def http_header(
  name: str = "",
  value: str = "",
) -> HTTPHeader:
  """
  HTTPHeader describes a custom header to be used in HTTP probes

  Args:
    name: The header field name
    value: The header field value
"""
  pass

def handler(
  exec: Optional[ExecAction] = None,
  http_get: Optional[HTTPGetAction] = None,
  tcp_socket: Optional[TCPSocketAction] = None,
) -> Handler:
  """
  Handler defines a specific action that should be taken in a probe.

  Args:
    exec: One and only one of the following should be specified.
      Exec specifies the action to take.
    http_get: HTTPGet specifies the http request to perform.
    tcp_socket: TCPSocket specifies an action involving a TCP port.
      TCP hooks not yet supported
      TODO: implement a realistic TCP lifecycle hook
"""
  pass

def ignore_def(
  base_path: str = "",
  patterns: List[str] = None,
) -> IgnoreDef:
  """
  Describes sets of file paths that the FileWatch should ignore.

  Args:
    base_path: BasePath is the base path for the patterns. It cannot be empty.
      
      If no patterns are specified, everything under it will be recursively ignored.
      
    patterns: Patterns are dockerignore style rules. Absolute-style patterns will be rooted to the BasePath.
      
      See https://docs.docker.com/engine/reference/builder/#dockerignore-file.
"""
  pass

def kubernetes_apply_cmd(
  args: List[str] = None,
  dir: str = "",
  env: List[str] = None,
) -> KubernetesApplyCmd:
  """
  

  Args:
    args: Args are the command-line arguments for the apply command. Must have length >= 1.
    dir: Process working directory.
      
      If not specified, will default to Tilt working directory.
      
    env: Env are additional variables for the process environment.
      
      Environment variables are layered on top of the environment variables
      that Tilt runs with.
      
"""
  pass

def kubernetes_discovery_template_spec(
  extra_selectors: List[LabelSelector] = None,
) -> KubernetesDiscoveryTemplateSpec:
  """
  

  Args:
    extra_selectors: ExtraSelectors are label selectors that will force discovery of a Pod even
      if it does not match the AncestorUID.
      
      This should only be necessary in the event that a CRD creates Pods but does
      not set an owner reference to itself.
"""
  pass

def kubernetes_image_locator(
  object_selector: ObjectSelector = None,
  path: str = "",
  object: Optional[KubernetesImageObjectDescriptor] = None,
) -> KubernetesImageLocator:
  """
  Finds image references in Kubernetes YAML.

  Args:
    object_selector: Selects which objects to look in.
    path: A JSON path to the image reference field.
      
      If Object is empty, the field should be a string.
      
      If Object is non-empty, the field should be an object with subfields.
    object: A descriptor of the path and structure of an object that describes an image
      reference. This is a common way to describe images in CRDs, breaking
      them down into an object rather than an image reference string.
      
"""
  pass

def kubernetes_image_object_descriptor(
  repo_field: str = "",
  tag_field: str = "",
) -> KubernetesImageObjectDescriptor:
  """
  

  Args:
    repo_field: The name of the field that contains the image repository.
    tag_field: The name of the field that contains the image tag.
"""
  pass

def kubernetes_watch_ref(
  uid: str = "",
  namespace: str = "",
  name: str = "",
) -> KubernetesWatchRef:
  """
  KubernetesWatchRef is similar to v1.ObjectReference from the Kubernetes API and is used to determine
  what objects should be reported on based on discovery.

  Args:
    uid: UID is a Kubernetes object UID.
      
      It should either be the exact object UID or the transitive owner.
      
    namespace: Namespace is the Kubernetes namespace for discovery. Required.
    name: Name is the Kubernetes object name.
      
      This is not directly used in discovery; it is extra metadata.
      
"""
  pass

def label_selector(
  match_labels: Dict[str, str] = None,
  match_expressions: List[LabelSelectorRequirement] = None,
) -> LabelSelector:
  """
  

  Args:
    match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
      map is equivalent to an element of matchExpressions, whose key field is "key", the
      operator is "In", and the values array contains only "value". The requirements are ANDed.
    match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
"""
  pass

def label_selector_requirement(
  key: str = "",
  operator: str = "",
  values: List[str] = None,
) -> LabelSelectorRequirement:
  """
  

  Args:
    key: key is the label key that the selector applies to.
    operator: operator represents a key's relationship to a set of values.
      Valid operators are In, NotIn, Exists and DoesNotExist.
    values: values is an array of string values. If the operator is In or NotIn,
      the values array must be non-empty. If the operator is Exists or DoesNotExist,
      the values array must be empty. This array is replaced during a strategic
      merge patch.
"""
  pass

def object_selector(
  api_version_regexp: str = "",
  kind_regexp: str = "",
  name_regexp: str = "",
  namespace_regexp: str = "",
) -> ObjectSelector:
  """
  Selector for any Kubernetes-style API.

  Args:
    api_version_regexp: A regular expression apiVersion match.
    kind_regexp: A regular expression kind match.
    name_regexp: A regular expression name match.
    namespace_regexp: A regular expression namespace match.
"""
  pass

def pod_log_stream_template_spec(
  only_containers: List[str] = None,
  ignore_containers: List[str] = None,
) -> PodLogStreamTemplateSpec:
  """
  PodLogStreamTemplateSpec describes common attributes for PodLogStreams
  that can be shared across pods.

  Args:
    only_containers: The names of containers to include in the stream.
      
      If `onlyContainers` and `ignoreContainers` are not set,
      will watch all containers in the pod.
      
    ignore_containers: The names of containers to exclude from the stream.
      
      If `onlyContainers` and `ignoreContainers` are not set,
      will watch all containers in the pod.
      
"""
  pass

def port_forward_template_spec(
  forwards: List[Forward] = None,
) -> PortForwardTemplateSpec:
  """
  PortForwardTemplateSpec describes common attributes for PortForwards
  that can be shared across pods.

  Args:
    forwards: One or more port forwards to execute on the given pod. Required.
"""
  pass

def probe(
  handler: Handler = None,
  initial_delay_seconds: int = 0,
  timeout_seconds: int = 0,
  period_seconds: int = 0,
  success_threshold: int = 0,
  failure_threshold: int = 0,
) -> Probe:
  """
  Probe describes a health check to be performed to determine whether it is
  alive or ready to receive traffic.

  Args:
    handler: The action taken to determine the health of a container
    initial_delay_seconds: Number of seconds after the container has started before liveness probes are initiated.
      More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    timeout_seconds: Number of seconds after which the probe times out.
      Defaults to 1 second. Minimum value is 1.
      More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    period_seconds: How often (in seconds) to perform the probe.
      Default to 10 seconds. Minimum value is 1.
    success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed.
      Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded.
      Defaults to 3. Minimum value is 1.
"""
  pass

def restart_on_spec(
  file_watches: List[str] = None,
  ui_buttons: List[str] = None,
) -> RestartOnSpec:
  """
  RestartOnSpec indicates the set of objects that can trigger a restart of this object.

  Args:
    file_watches: FileWatches that can trigger a restart.
    ui_buttons: UIButtons that can trigger a restart.
"""
  pass

def start_on_spec(
  ui_buttons: List[str] = None,
) -> StartOnSpec:
  """
  StartOnSpec indicates the set of objects that can trigger a start/restart of this object.

  Args:
    ui_buttons: UIButtons that can trigger a start/restart.
"""
  pass

def tcp_socket_action(
  port: int = 0,
  host: str = "",
) -> TCPSocketAction:
  """
  TCPSocketAction describes an action based on opening a socket

  Args:
    port: Number or name of the port to access on the container.
      Number must be in the range 1 to 65535.
    host: Optional: Host name to connect to, defaults to the pod IP.
"""
  pass

def ui_bool_input_spec(
  default_value: bool = False,
  true_string: Optional[str] = None,
  false_string: Optional[str] = None,
) -> UIBoolInputSpec:
  """
  Describes a boolean checkbox input field attached to a button.

  Args:
    default_value: Whether the input is initially true or false.
    true_string: If the input's value is converted to a string, use this when the value is true.
      If unspecified, its string value will be `"true"`
    false_string: If the input's value is converted to a string, use this when the value is false.
      If unspecified, its string value will be `"false"`
"""
  pass

def ui_component_location(
  component_id: str = "",
  component_type: str = "",
) -> UIComponentLocation:
  """
  UIComponentLocation specifies where to put a UI component.

  Args:
    component_id: ComponentID is the identifier of the parent component to associate this component with.
      
      For example, this is a resource name if the ComponentType is Resource.
    component_type: ComponentType is the type of the parent component.
"""
  pass

def ui_hidden_input_spec(
  value: str = "",
) -> UIHiddenInputSpec:
  """
  Describes a hidden input field attached to a button,
  with a value to pass on any submit.

  Args:
    value: Documentation missing
"""
  pass

def ui_input_spec(
  name: str = "",
  label: str = "",
  text: Optional[UITextInputSpec] = None,
  bool: Optional[UIBoolInputSpec] = None,
  hidden: Optional[UIHiddenInputSpec] = None,
) -> UIInputSpec:
  """
  Defines an Input to render in the UI.
  If UIButton is analogous to an HTML <form>,
  UIInput is analogous to an HTML <input>.

  Args:
    name: Name of this input. Must be unique within the UIButton.
    label: A label to display next to this input in the UI.
    text: A Text input that takes a string.
    bool: A Bool input that is true or false
    hidden: An input that has a constant value and does not display to the user
"""
  pass

def ui_text_input_spec(
  default_value: str = "",
  placeholder: str = "",
) -> UITextInputSpec:
  """
  Describes a text input field attached to a button.

  Args:
    default_value: Initial value for this field.
      
    placeholder: A short hint that describes the expected input of this field.
      
"""
  pass